"""Write SQL from the tracking plan. Pure functions: no BigQuery here."""
from itertools import combinations


def item_present(field: str, field_type: str) -> str:
    """Write the SQL condition for an items field being filled in."""
    condition = f"item.{field} IS NOT NULL"
    if field_type == "string":
        condition += f" AND item.{field} != '(not set)'"
    return condition


def field_present(location: str, field: str, field_type: str = "") -> str:
    """Write the SQL condition for an event_params, ecommerce or items field being sent."""
    if location == "event_params":
        return f"EXISTS(SELECT 1 FROM UNNEST(event_params) WHERE key = '{field}')"
    if location == "items":
        return f"EXISTS(SELECT 1 FROM UNNEST(items) AS item WHERE {item_present(field, field_type)})"
    return f"{location}.{field} IS NOT NULL"


def daily_coverage_sql(fields: list[tuple[str, str, str, str]]) -> str:
    """Write SQL counting, per day, the events that sent each field. Fields are (event_name, location, field_name, type)."""
    blocks = []
    for event, location, field, field_type in fields:
        has_products = " AND ARRAY_LENGTH(items) > 0" if location == "items" else ""
        blocks.append(
            f"SELECT event_date, event_name, '{field}' AS field_name, "
            f"COUNTIF({field_present(location, field, field_type)}) AS present, COUNT(*) AS total "
            "FROM `{table}` WHERE _TABLE_SUFFIX BETWEEN '{start_date}' AND '{end_date}' "
            f"AND event_name = '{event}'{has_products} GROUP BY event_date, event_name"
        )
    return "\nUNION ALL\n".join(blocks)


def co_missing_sql(event: str, fields: list[tuple[str, str, str]]) -> str:
    """Write SQL counting events missing each pair of fields, alone and together. Fields are (location, field_name, type)."""
    flags = ", ".join(
        f"NOT {field_present(location, field, field_type)} AS {field}"
        for location, field, field_type in fields
    )
    blocks = [
        f"SELECT '{event}' AS event_name, '{a}' AS field_a, '{b}' AS field_b, "
        f"COUNTIF({a}) AS missing_a, COUNTIF({b}) AS missing_b, COUNTIF({a} AND {b}) AS missing_both FROM flags"
        for a, b in combinations([field for _, field, _ in fields], 2)
    ]
    return (
        f"WITH flags AS (SELECT {flags} FROM `{{table}}` "
        f"WHERE _TABLE_SUFFIX BETWEEN '{{start_date}}' AND '{{end_date}}' AND event_name = '{event}')\n"
        + "\nUNION ALL\n".join(blocks)
    )


def items_coverage_per_product_sql(fields: list[tuple[str, str]]) -> str:
    """Write SQL for the share of products with each items field filled in, per event."""
    blocks = [
        f"SELECT event_name, '{field}' AS field_name, "
        f"SAFE_DIVIDE(COUNTIF({item_present(field, field_type)}), COUNT(*)) AS coverage_rate "
        "FROM item_rows GROUP BY event_name"
        for field, field_type in fields
    ]
    return (
        "WITH item_rows AS (SELECT event_name, item FROM `{table}`, UNNEST(items) AS item "
        "WHERE _TABLE_SUFFIX BETWEEN '{start_date}' AND '{end_date}')\n"
        + "\nUNION ALL\n".join(blocks)
    )


def items_coverage_per_event_sql(fields: list[tuple[str, str]]) -> str:
    """Write SQL for the share of events with at least one product that has each items field."""
    blocks = [
        f"SELECT event_name, '{field}' AS field_name, "
        f"SAFE_DIVIDE(COUNTIF(EXISTS(SELECT 1 FROM UNNEST(items) AS item WHERE {item_present(field, field_type)})), COUNT(*)) AS coverage_rate "
        "FROM `{table}` WHERE _TABLE_SUFFIX BETWEEN '{start_date}' AND '{end_date}' AND ARRAY_LENGTH(items) > 0 "
        "GROUP BY event_name"
        for field, field_type in fields
    ]
    return "\nUNION ALL\n".join(blocks)


def value_type_sql(fields: list[tuple[str, str]]) -> str:
    """Write SQL counting, per day, the event_params values sent as text and as numbers. Fields are (event_name, field_name)."""
    pairs = " OR ".join(f"(event_name = '{event}' AND param.key = '{field}')" for event, field in fields)
    return (
        "SELECT event_date, event_name, param.key AS field_name, "
        "COUNTIF(param.value.string_value IS NOT NULL) AS text_values, "
        "COUNTIF(param.value.int_value IS NOT NULL OR param.value.double_value IS NOT NULL OR param.value.float_value IS NOT NULL) AS number_values, "
        "COUNT(*) AS total "
        "FROM `{table}`, UNNEST(event_params) AS param "
        "WHERE _TABLE_SUFFIX BETWEEN '{start_date}' AND '{end_date}' "
        f"AND ({pairs}) GROUP BY event_date, event_name, field_name"
    )

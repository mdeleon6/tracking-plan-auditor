"""Write SQL from the tracking plan. Pure functions: no BigQuery here."""


def item_present(field: str, field_type: str) -> str:
    """Write the SQL condition for an items field being filled in."""
    condition = f"item.{field} IS NOT NULL"
    if field_type == "string":
        condition += f" AND item.{field} != '(not set)'"
    return condition


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

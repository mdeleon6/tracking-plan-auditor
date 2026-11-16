from build_sql import (
    co_missing_sql,
    daily_coverage_sql,
    field_present,
    item_present,
    value_type_sql,
)


def test_item_present_for_text_excludes_not_set():
    assert item_present("item_name", "string") == "item.item_name IS NOT NULL AND item.item_name != '(not set)'"


def test_item_present_for_numbers_only_checks_null():
    assert item_present("price", "number") == "item.price IS NOT NULL"


def test_field_present_for_event_params_checks_the_key():
    assert field_present("event_params", "transaction_id") == "EXISTS(SELECT 1 FROM UNNEST(event_params) WHERE key = 'transaction_id')"


def test_field_present_for_ecommerce_checks_null():
    assert field_present("ecommerce", "purchase_revenue") == "ecommerce.purchase_revenue IS NOT NULL"


def test_daily_coverage_sql_counts_each_field_per_day():
    sql = daily_coverage_sql([("purchase", "event_params", "transaction_id", "string"), ("purchase", "ecommerce", "purchase_revenue", "number")])
    assert sql.count("UNION ALL") == 1
    assert "COUNTIF(ecommerce.purchase_revenue IS NOT NULL) AS present" in sql
    assert "AND event_name = 'purchase' GROUP BY event_date" in sql


def test_daily_coverage_sql_only_counts_events_with_products_for_items_fields():
    sql = daily_coverage_sql([("add_to_cart", "items", "quantity", "number")])
    assert "AND event_name = 'add_to_cart' AND ARRAY_LENGTH(items) > 0 GROUP BY" in sql


def test_field_present_for_items_checks_any_product():
    assert field_present("items", "quantity", "number") == "EXISTS(SELECT 1 FROM UNNEST(items) AS item WHERE item.quantity IS NOT NULL)"


def test_co_missing_sql_counts_each_pair_once():
    sql = co_missing_sql("purchase", [("event_params", "transaction_id", "string"), ("event_params", "tax", "number"), ("ecommerce", "purchase_revenue", "number")])
    assert sql.count("UNION ALL") == 2
    assert "NOT ecommerce.purchase_revenue IS NOT NULL AS purchase_revenue" in sql
    assert "COUNTIF(transaction_id AND tax) AS missing_both" in sql


def test_value_type_sql_only_counts_planned_pairs():
    sql = value_type_sql([("purchase", "transaction_id"), ("add_to_cart", "ga_session_id")])
    assert "(event_name = 'purchase' AND param.key = 'transaction_id') OR (event_name = 'add_to_cart' AND param.key = 'ga_session_id')" in sql
    assert "COUNTIF(param.value.string_value IS NOT NULL) AS text_values" in sql
    assert sql.endswith("GROUP BY event_date, event_name, field_name")

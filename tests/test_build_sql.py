from build_sql import item_present


def test_item_present_for_text_excludes_not_set():
    assert item_present("item_name", "string") == "item.item_name IS NOT NULL AND item.item_name != '(not set)'"


def test_item_present_for_numbers_only_checks_null():
    assert item_present("price", "number") == "item.price IS NOT NULL"

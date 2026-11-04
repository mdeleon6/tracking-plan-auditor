from checks import compare_events


def test_finds_missing_and_unplanned_events():
    planned = {"event1", "event2", "event3"}
    observed = {"event2", "event4"}
    result = compare_events(planned, observed)
    assert result["missing_in_data"] == {"event1", "event3"}
    assert result["not_in_plan"] == {"event4"}


def test_no_differences():
    result = compare_events({"a", "b"}, {"a", "b"})
    assert result["missing_in_data"] == set()
    assert result["not_in_plan"] == set()


def test_nothing_observed():
    result = compare_events({"a", "b"}, set())
    assert result["missing_in_data"] == {"a", "b"}
    assert result["not_in_plan"] == set()
from checks import compare_events, find_deprecated_events


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
    
    
def test_deprecated_event_still_firing():
    deprecated = {"event1", "event2"}
    observed = {"event2", "event3"}
    result = find_deprecated_events(deprecated, observed)
    assert result == {"event2"}
    
    
def test_deprecated_event_stopped():
    deprecated = {"event1", "event2"}
    observed = {"event3", "event4"}
    result = find_deprecated_events(deprecated, observed)
    assert result == set()
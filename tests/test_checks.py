from checks import compare_events, find_deprecated_events, audit_events, find_field_gaps
import pandas as pd


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
    

def test_deprecated_event_is_only_reported_once():
    plan = pd.DataFrame({
        "event_name": ["page_view", "old_event"],
        "status": ["active", "deprecated"],
    })
    observed = {"page_view", "old_event"}
    
    result = audit_events(plan, observed)
    assert result["deprecated_still_firing"] == {"old_event"}
    assert result["not_in_plan"] == set()
    
    
def test_field_gaps_finds_low_and_missing_fields():
    required = pd.DataFrame({
        "event_name": ["purchase", "purchase", "purchase"],
        "field_name": ["value", "tax", "currency"],
    })
    coverage = pd.DataFrame({
        "event_name": ["purchase", "purchase"],
        "field_name": ["value", "tax"],
        "coverage_rate": [1.0, 0.92],
    })

    gaps = find_field_gaps(required, coverage)

    assert set(gaps["field_name"]) == {"tax", "currency"}

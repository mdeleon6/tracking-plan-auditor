from checks import compare_events, find_deprecated_events, audit_events, find_field_gaps, find_missing_days, find_low_days
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


def test_finds_days_an_event_is_missing():
    daily = pd.DataFrame({
        "event_date": ["20201101", "20201102", "20201103", "20201101", "20201103"],
        "event_name": ["page_view", "page_view", "page_view", "add_to_cart", "add_to_cart"],
        "event_count": [100, 120, 90, 10, 8],
    })

    result = find_missing_days(daily)

    assert result == {"add_to_cart": {"20201102"}}
    

def test_finds_low_days_compared_with_same_weekday():
    daily = pd.DataFrame({
        "event_date": [
            "20201101", "20201108", "20201115", "20201122", "20201129",
            "20201102", "20201109", "20201116",
        ],
        "event_name": ["page_view"] * 8,
        "event_count": [100, 110, 10, 105, 95, 30, 32, 28],
    })

    low = find_low_days(daily)

    assert set(low["event_date"]) == {"20201115"}
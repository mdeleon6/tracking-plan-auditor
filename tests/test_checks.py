from checks import compare_events, find_deprecated_events, audit_events, find_field_gaps, find_missing_days, find_low_days, find_co_missing
from ai_tickets import describe_field_gaps, find_unsupported_numbers, group_consecutive_dates, describe_missing_days, split_low_days, describe_low_days_by_event, describe_low_days_together, format_day_with_holiday
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
        "measured_per": ["event", "event", "event"],
    })
    coverage = pd.DataFrame({
        "event_name": ["purchase", "purchase"],
        "field_name": ["value", "tax"],
        "measured_per": ["event", "event"],
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
    
    
def test_groups_fields_with_same_event_and_rate():
    gaps = pd.DataFrame({
        "event_name": ["purchase", "purchase", "purchase"],
        "field_name": ["value", "tax", "shipping_tier"],
        "location": ["event_params", "event_params", "event_params"],
        "coverage_rate": [0.92, 0.92, 0.73],
        "measured_per": ["event", "event", "event"],
    })
    co_missing = pd.DataFrame({
        "event_name": ["purchase", "add_to_cart"],
        "field_a": ["value", "value"],
        "field_b": ["shipping_tier", "shipping_tier"],
        "missing_a": [8, 3],
        "missing_b": [27, 3],
        "missing_both": [8, 3],
    })

    problems = describe_field_gaps(gaps, {("purchase", "value"): "revenue"}, co_missing)

    assert len(problems) == 2
    assert any("Gap to threshold: 7.0 percentage points" in p for p in problems)
    assert any("used in: revenue" in p for p in problems)
    assert all("Records missing both value and shipping_tier: 8 " in p for p in problems)
    assert not any(": 3 (" in p for p in problems)



def test_flags_numbers_not_in_the_input():
    problem = "Coverage is 92.1 and the threshold is 99."
    ticket = "Coverage is 92.1, which is 7.5 below 99."

    assert find_unsupported_numbers(ticket, problem) == {"7.5"}


def test_groups_consecutive_dates_into_stretches():
    dates = {"20201231", "20210101", "20210105"}

    result = group_consecutive_dates(dates)

    assert result == [
        (pd.Timestamp("2020-12-31"), pd.Timestamp("2021-01-01")),
        (pd.Timestamp("2021-01-05"), pd.Timestamp("2021-01-05")),
    ]


def test_describes_missing_days_with_counts_and_stretches():
    daily = pd.DataFrame({
        "event_date": ["20201101", "20201102", "20201103", "20201104"],
        "event_name": ["purchase", "purchase", "purchase", "purchase"],
        "event_count": [5, 5, 5, 5],
    })
    missing = {"add_to_cart": {"20201102", "20201103"}}

    problems = describe_missing_days(missing, daily, {"add_to_cart": "high"}, {})

    assert len(problems) == 1
    assert "Days with no data for this event: 2 of 4." in problems[0]
    assert "- Nov 2, 2020 to Nov 3, 2020" in problems[0]
    assert "Events with data on every day of the period: purchase." in problems[0]
    assert "Severity set by the tracking plan: High." in problems[0]


def test_describes_dates_shared_with_other_events():
    daily = pd.DataFrame({
        "event_date": ["20201101", "20201102", "20201103", "20201104"],
        "event_name": ["purchase", "purchase", "purchase", "purchase"],
        "event_count": [5, 5, 5, 5],
    })
    missing = {
        "add_to_cart": {"20201102", "20201103"},
        "select_item": {"20201103", "20201104"},
    }

    problems = describe_missing_days(missing, daily, {}, {})

    assert "select_item also has no data on 1 of these days: Nov 3, 2020." in problems[0]
    assert "add_to_cart also has" not in problems[0]
    assert "Severity set by the tracking plan: Not rated." in problems[0]


def test_splits_days_when_many_events_drop_together():
    low = pd.DataFrame({
        "event_date": ["20201224", "20201224", "20201224", "20201105"],
        "event_name": ["purchase", "view_item", "add_to_cart", "purchase"],
    })

    together, separate = split_low_days(low, min_events=3)

    assert len(together) == 3
    assert set(together["event_date"]) == {"20201224"}
    assert len(separate) == 1
    assert list(separate["event_date"]) == ["20201105"]


def test_describes_low_days_for_one_event():
    separate = pd.DataFrame({
        "event_date": ["20201105", "20210105"],
        "event_name": ["purchase", "purchase"],
        "event_count": [26, 29],
        "typical": [54.0, 60.0],
    })
    separate["ratio"] = separate["event_count"] / separate["typical"]
    together = pd.DataFrame({
        "event_date": ["20201224", "20201225", "20201224"],
        "event_name": ["purchase", "purchase", "view_item"],
    })
    missing = {"purchase": {"20201201", "20201202"}}

    problems = describe_low_days_by_event(separate, together, missing, {"purchase": "high"}, {}, {"purchase": "orders, revenue"})
    problem = problems[0]

    assert len(problems) == 1
    assert "Tracking plan rating if this event stopped arriving entirely: High." in problem
    assert "- Nov 5, 2020: 26 events, typical 54, 48.1% of typical" in problem
    assert problem.count("This event was also below threshold") == 1
    assert "Dec 24, 2020, Dec 25, 2020." in problem
    assert "This event also has days with no data at all: Dec 1, 2020 to Dec 2, 2020." in problem
    assert "Date ranges are not checked against the calendar." in problem
    assert "Used in, according to the tracking plan: orders, revenue." in problem
    assert "covered in a separate missing-day ticket" in problem



def test_describes_days_when_many_events_drop_together():
    together = pd.DataFrame({
        "event_date": ["20201224", "20201224", "20201225"],
        "event_name": ["purchase", "view_item", "purchase"],
        "ratio": [0.3, 0.4, 0.2],
    })
    severities = {"purchase": "high", "view_item": "medium"}
    holidays = {"20201224": "Christmas Eve", "20201225": "Christmas Day"}
    uses = {"purchase": "orders"}

    problem = describe_low_days_together(together, severities, holidays, uses)[0]

    assert "Days listed: 2. Different events affected: 2." in problem
    assert "rated High in the tracking plan if they stopped arriving entirely: purchase." in problem
    assert "- Dec 24, 2020 (Christmas Eve): 2 events below threshold: purchase 30.0%, view_item 40.0%" in problem
    assert "used in, according to the tracking plan: purchase: orders." in problem

    no_ratings = describe_low_days_together(together, {}, holidays, uses)[0]
    assert "if they stopped arriving entirely: none." in no_ratings
    assert describe_low_days_together(together.iloc[0:0], severities, holidays, uses) == []


def test_adds_holiday_name_to_date():
    holidays = {"20201224": "Christmas Eve"}

    assert format_day_with_holiday("20201224", holidays) == "Dec 24, 2020 (Christmas Eve)"
    assert format_day_with_holiday("20201105", holidays) == "Nov 5, 2020"


def test_field_gaps_uses_the_plans_measurement():
    required = pd.DataFrame({
        "event_name": ["add_to_cart"],
        "field_name": ["quantity"],
        "measured_per": ["event"],
    })
    coverage = pd.DataFrame({
        "event_name": ["add_to_cart", "add_to_cart"],
        "field_name": ["quantity", "quantity"],
        "measured_per": ["product", "event"],
        "coverage_rate": [0.06, 0.64],
    })

    gaps = find_field_gaps(required, coverage)

    assert list(gaps["coverage_rate"]) == [0.64]
    
    
def test_counts_records_missing_two_fields_together():
    records = pd.DataFrame({
        "keys": [
            ["transaction_id", "shipping_tier"],
            ["shipping_tier"],
            [],
            ["transaction_id"],
        ],
    })

    result = find_co_missing(records, ["transaction_id", "shipping_tier"])
    row = result.iloc[0]

    assert row["missing_a"] == 2
    assert row["missing_b"] == 2
    assert row["missing_both"] == 1

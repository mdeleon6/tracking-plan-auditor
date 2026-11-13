"""Turn check results into problem descriptions: the text Claude writes tickets from."""
import pandas as pd


def group_consecutive_dates(dates: set[str]) -> list[tuple[pd.Timestamp, pd.Timestamp]]:
    """Turn a set of YYYYMMDD dates into (first day, last day) stretches."""
    days = sorted(pd.to_datetime(list(dates), format="%Y%m%d"))
    stretches = []
    start = days[0]
    previous = days[0]

    for day in days[1:]:
        if (day - previous).days != 1:
            stretches.append((start, previous))
            start = day
        previous = day

    stretches.append((start, previous))
    return stretches


def format_day(day: pd.Timestamp) -> str:
    """Write a date like Nov 2, 2020."""
    return f"{day:%b} {day.day}, {day.year}"


def format_stretch(start: pd.Timestamp, end: pd.Timestamp) -> str:
    """Write a stretch of dates, or one date if it starts and ends on the same day."""
    if start == end:
        return format_day(start)
    return f"{format_day(start)} to {format_day(end)}"


def format_day_with_holiday(event_date: str, holidays: dict[str, str]) -> str:
    """Format a YYYYMMDD date, adding the holiday name if the calendar has one."""
    day = pd.to_datetime(event_date, format="%Y%m%d")
    holiday = holidays.get(event_date)
    if holiday:
        return f"{format_day(day)} ({holiday})"
    return format_day(day)


def describe_missing_days(missing: dict[str, set[str]], daily: pd.DataFrame, severities: dict[str, str], uses: dict[str, str]) -> list[str]:
    """Write one problem description per event that has days with no data."""
    days = pd.to_datetime(daily["event_date"], format="%Y%m%d")
    period = format_stretch(days.min(), days.max())
    total_days = days.nunique()

    complete_events = sorted(set(daily["event_name"]) - set(missing.keys()))


    problems = []
    for event_name, gaps in missing.items():
        severity = severities.get(event_name, "not rated").capitalize()
        event_rows = daily[daily["event_name"] == event_name]
        total_events = event_rows["event_count"].astype(int).sum()
        days_with_data = total_days - len(gaps)
        stretches = group_consecutive_dates(gaps)
        lines = [
            "Check: missing days. An event is flagged for any day in the data period when it has no rows.",
            f"Event: {event_name}",
            f"Severity set by the tracking plan: {severity}.",
            f"Used in, according to the tracking plan: {uses.get(event_name, 'not listed')}.",
            f"Data period: {period} ({total_days} days).",
            f"Total events received on the {days_with_data} days with data: {total_events}.",
            f"Days with no data for this event: {len(gaps)} of {total_days}.",
            "At least one other event was received on every one of these days.",
            f"Events with data on every day of the period: {', '.join(complete_events)}.",
            "Dates with no data:",
        ]
        for start, end in stretches:
            lines.append(f"- {format_stretch(start, end)}")
        for other_event, other_gaps in missing.items():
            shared = gaps & other_gaps
            if other_event != event_name and shared:
                shared_stretches = group_consecutive_dates(shared)
                shared_dates = "; ".join(format_stretch(start, end) for start, end in shared_stretches)
                lines.append(
                    f"{other_event} also has no data on {len(shared)} of these days: {shared_dates}. "
                    f"Across the whole period, {other_event} has no data on {len(other_gaps)} days."
                )
        problems.append("\n".join(lines))
    return problems


def describe_field_gaps(gaps: pd.DataFrame, uses: dict[tuple[str, str], str], co_missing: pd.DataFrame, drops: pd.DataFrame, shifts: pd.DataFrame | None = None, period: str | None = None, min_coverage: float = 0.99) -> list[str]:
    """Group field gaps into problem descriptions, one per event and coverage rate."""
    problems = []
    for (event_name, rate), rows in gaps.groupby(["event_name", "coverage_rate"]):
        missing = round((1 - rate) * 100, 4)
        gap = round((min_coverage - rate) * 100, 4)
        lines = [
            f"Check: required field coverage. A field is flagged when coverage is below {min_coverage}.",
            f"Event: {event_name}",
            f"Share of events or products missing each field: {missing}%. Gap to threshold: {gap} percentage points.",
            f"Flagged fields, all with coverage_rate {round(rate, 6)}:",
        ]
        if period is not None:
            lines.insert(1, f"Data period: {period}.")
        for _, row in rows.iterrows():
            unit = row["measured_per"]
            used = uses.get((event_name, row["field_name"]), "not listed")
            lines.append(f"- {row['field_name']} (location: {row['location']}, measured per {unit}; used in: {used})")
        if ((rows["location"] == "items") & (rows["measured_per"] == "event")).any():
            lines.append("The tracking plan expects these fields on one product per event, the product actually added, so an event counts as covered if at least one of its products has the field.")
        fields = set(rows["field_name"])
        linked = co_missing[
            (co_missing["event_name"] == event_name)
            & (co_missing["missing_both"] > 0)
            & (co_missing["field_a"].isin(fields) | co_missing["field_b"].isin(fields))
        ]
        for _, pair in linked.iterrows():
            lines.append(
                f"Records missing both {pair['field_a']} and {pair['field_b']}: {pair['missing_both']} "
                f"({pair['field_a']} missing on {pair['missing_a']}, {pair['field_b']} missing on {pair['missing_b']})."
            )
        lines.extend(describe_coverage_drops(drops, event_name, fields))
        if shifts is not None:
            lines.extend(describe_coverage_shifts(shifts, event_name, fields))
        problems.append("\n".join(lines))
    return problems


def describe_coverage_drops(drops: pd.DataFrame, event_name: str, fields: set[str], max_drop: float = 0.10) -> list[str]:
    """Write lines listing the stretches of days when each field's coverage dropped."""
    rows = drops[(drops["event_name"] == event_name) & drops["field_name"].isin(fields)]
    if rows.empty:
        return []
    by_text = {}
    for field, days in rows.groupby("field_name"):
        dates = pd.to_datetime(days["event_date"], format="%Y%m%d")
        parts = []
        for start, end in group_consecutive_dates(set(days["event_date"])):
            stretch = days[(dates >= start) & (dates <= end)]
            present, total = int(stretch["present"].sum()), int(stretch["total"].sum())
            parts.append(f"{format_stretch(start, end)}: {present} of {total} ({round(present / total * 100, 1)}%)")
        typical = round(days["typical"].iloc[0] * 100, 1)
        missing_on_days = int((days["total"] - days["present"]).sum())
        text = f"(typical daily coverage {typical}%, {missing_on_days} missing records on these days): " + "; ".join(parts)
        by_text.setdefault(text, []).append(field)
    lines = [f"Days when coverage was more than {round(max_drop * 100)} percentage points below the field's typical daily coverage:"]
    for text, names in by_text.items():
        lines.append(f"- {', '.join(names)} {text}")
    return lines


def describe_coverage_shifts(shifts: pd.DataFrame, event_name: str, fields: set[str], window: int = 7, max_drop: float = 0.10) -> list[str]:
    """Write lines listing days when coverage fell well below the previous days' median."""
    rows = shifts[(shifts["event_name"] == event_name) & shifts["field_name"].isin(fields)]
    if rows.empty:
        return []
    lines = [
        f"Days when coverage was more than {round(max_drop * 100)} percentage points below the median of the previous {window} days with data. "
        "A flagged day can mark where a lasting change starts: once the lower level becomes normal, later days are not flagged.",
    ]
    for _, row in rows.iterrows():
        day = format_day(pd.to_datetime(row["event_date"], format="%Y%m%d"))
        coverage = round(row["coverage"] * 100, 1)
        before = round(row["before"] * 100, 1)
        if pd.isna(row["after"]):
            after = "none in the data"
        elif row["after"] >= row["before"] - max_drop:
            after = f"{round(row['after'] * 100, 1)}%, back within {round(max_drop * 100)} points of the previous median"
        else:
            after = f"{round(row['after'] * 100, 1)}%, still more than {round(max_drop * 100)} points below the previous median"
        lines.append(f"- {row['field_name']} on {day}: {row['present']} of {row['total']} ({coverage}%), previous {window} days' median {before}%, next day with data {after}")
    return lines


def describe_dependency_breaks(breaks: pd.DataFrame, uses: dict[str, str]) -> list[str]:
    """Write one problem description per event that fired more often than the event it requires."""
    problems = []
    for _, row in breaks.iterrows():
        event, required = row["event_name"], row["requires"]
        lines = [
            "Check: event dependencies. A pair is flagged when an event fires more often over the period than the event it requires.",
            f"Event: {event}",
            f"Requires: {required}, because {row['reason']}.",
            f"{event} fired {row['event_count']} times. {required} fired {row['required_count']} times.",
        ]
        if row["required_count"] > 0:
            times = round(row["event_count"] / row["required_count"], 1)
            lines.append(f"{event} fired {times} times as often as {required}.")
        else:
            lines.append(f"{required} never fired.")
        lines.append(f"Used in, according to the tracking plan: {event}: {uses.get(event, 'not listed')}; {required}: {uses.get(required, 'not listed')}.")
        problems.append("\n".join(lines))
    return problems


def describe_repeated_item_counts(repeated: pd.DataFrame, uses: dict[str, str], checked: set[str], period: str) -> list[str]:
    """Write one problem description for events where most records carry the same number of products."""
    if repeated.empty:
        return []
    lines = [
        "Check: repeated product counts. An event is flagged when most of its records with products carry the same number of products, above 1.",
        f"Data period: {period}.",
        "The tracking plan does not say how many products each event should carry.",
    ]
    for _, row in repeated.iterrows():
        event = row["event_name"]
        percent = round(row["share"] * 100, 1)
        lines.append(
            f"- {event}: {row['events']} of {row['total']} records with products ({percent}%) carry exactly {row['items_in_event']} products. "
            f"No record carries more than {row['max_items']}. Used in, according to the tracking plan: {uses.get(event, 'not listed')}."
        )
    not_flagged = sorted(checked - set(repeated["event_name"]))
    lines.append(f"Checked and not flagged: {', '.join(not_flagged)}.")
    return ["\n".join(lines)]


def describe_low_days_by_event(
    separate: pd.DataFrame,
    together: pd.DataFrame,
    missing: dict[str, set[str]],
    severities: dict[str, str],
    holidays: dict[str, str],
    uses: dict[str, str],
    min_ratio: float = 0.5,
) -> list[str]:
    """Write one problem description per event with low days."""
    problems = []
    for event_name, rows in separate.groupby("event_name"):
        rating = severities.get(event_name, "not rated").capitalize()
        lines = [
            f"Check: low volume. A day is flagged when an event's count is below {min_ratio} of its typical count, meaning the median for that weekday.",
            f"Event: {event_name}",
            f"Tracking plan rating if this event stopped arriving entirely: {rating}.",
            f"Used in, according to the tracking plan: {uses.get(event_name, 'not listed')}.",
            f"Number of flagged days: {len(rows)}.",
            "Holiday names next to dates come from the holiday calendar in the tracking plan, followed by where each holiday is observed as a day off. A single date without a name is not on that calendar. Date ranges are not checked against the calendar.",
            "Flagged days:",
        ]
        for _, row in rows.sort_values("event_date").iterrows():
            percent = round(row["ratio"] * 100, 1)
            lines.append(f"- {format_day_with_holiday(row['event_date'], holidays)}: {row['event_count']} events, typical {row['typical']:g}, {percent}% of typical")
        
        grouped_days = sorted(together[together["event_name"] == event_name]["event_date"])
        if grouped_days:
            days = ", ".join(format_day_with_holiday(d, holidays) for d in grouped_days)
            lines.append(
                f"This event was also below threshold on {len(grouped_days)} more days when many events dropped together. "
                f"Those days are covered in a separate multi-event ticket: {days}."
            )

        if event_name in missing:
            stretches = group_consecutive_dates(missing[event_name])
            dates = "; ".join(format_stretch(start, end) for start, end in stretches)
            lines.append(
                f"This event also has days with no data at all: {dates}. "
                "Those days are covered in a separate missing-day ticket and are not part of this one."
            )

        problems.append("\n".join(lines))
    return problems


def describe_low_days_together(
    together: pd.DataFrame,
    severities: dict[str, str],
    holidays: dict[str, str],
    uses: dict[str, str],
    min_events: int = 5,
    min_ratio: float = 0.5,
) -> list[str]:
    """Write one problem description for days when many events dropped together."""
    if together.empty:
        return []

    events = sorted(together["event_name"].unique())
    high_events = [event for event in events if severities.get(event) == "high"]
    high_uses = "; ".join(f"{event}: {uses[event]}" for event in high_events if event in uses)
    lines = [
        f"Check: low volume across many events. A day is listed when at least {min_events} events are each below {min_ratio} of their typical count, meaning the median for that weekday.",
        "Event: multiple events",
        f"Days listed: {together['event_date'].nunique()}. Different events affected: {len(events)}.",
        f"Affected events rated High in the tracking plan if they stopped arriving entirely: {', '.join(high_events) or 'none'}.",
        f"What the High-rated events are used in, according to the tracking plan: {high_uses or 'none'}.",
        "Holiday names next to dates come from the holiday calendar in the tracking plan, followed by where each holiday is observed as a day off. A single date without a name is not on that calendar. Date ranges are not checked against the calendar.",
        "Days listed, with each affected event's count as a percentage of its typical count:",
    ]
    for event_date, rows in together.groupby("event_date"):
        drops = ", ".join(
            f"{row['event_name']} {round(row['ratio'] * 100, 1)}%"
            for _, row in rows.sort_values("event_name").iterrows()
        )
        lines.append(f"- {format_day_with_holiday(event_date, holidays)}: {len(rows)} events below threshold: {drops}")

    return ["\n".join(lines)]

"""Show the results of every check."""
import pandas as pd
import streamlit as st

from run_checks import run_all_checks


@st.cache_data(ttl="1h", show_spinner="Running the checks in BigQuery...")
def load_results() -> dict:
    """Run every check once and reuse the results for an hour."""
    return run_all_checks()


st.title("Results")
if st.button("Run audit", type="primary", icon=":material/play_arrow:"):
    st.session_state["results"] = load_results()

if "results" not in st.session_state:
    st.info("Run the audit to see results.")
    st.stop()

results = st.session_state["results"]
with st.container(horizontal=True):
    st.metric("Field gaps", len(results["field_gaps"]), border=True)
    st.metric("Type mismatch days", len(results["type_mismatches"]), border=True)
    st.metric("Low days", len(results["low_days"]), border=True)
    st.metric("Planned events never received", len(results["events"]["missing_in_data"]), border=True)

events, fields, coverage, volume, types, rules = st.tabs(["Events", "Fields", "Coverage", "Volume", "Types", "Rules"])
with events:
    groups = [
        ("Planned but never received", "missing_in_data"),
        ("Sent but not in the plan", "not_in_plan"),
        ("Deprecated but still sent", "deprecated_still_firing"),
    ]
    with st.container(horizontal=True):
        for title, key in groups:
            with st.container(border=True):
                st.subheader(title)
                names = sorted(results["events"][key])
                st.markdown("\n".join(f"- `{name}`" for name in names) or "None")
with fields:
    st.subheader("Required fields below 99%")
    st.dataframe(
        results["field_gaps"],
        hide_index=True,
        alt="Required fields below 99% coverage",
        column_config={
            "event_name": "Event",
            "field_name": "Field",
            "location": "Location",
            "measured_per": "Measured per",
            "coverage_rate": st.column_config.ProgressColumn("Coverage", format="percent", min_value=0, max_value=1),
            "never_seen": st.column_config.CheckboxColumn("Never seen"),
        },
    )
with coverage:
    percent = {"format": "percent"}
    st.subheader("Days far below the field's usual coverage")
    st.dataframe(
        results["coverage_drops"],
        hide_index=True,
        alt="Days far below the field's usual coverage",
        column_order=["event_date", "event_name", "field_name", "present", "total", "coverage", "typical"],
        column_config={
            "event_date": "Date",
            "event_name": "Event",
            "field_name": "Field",
            "present": st.column_config.NumberColumn("Sent"),
            "total": st.column_config.NumberColumn("Events"),
            "coverage": st.column_config.NumberColumn("Coverage", **percent),
            "typical": st.column_config.NumberColumn("Usual coverage", **percent),
        },
    )
    st.subheader("Days far below the week before")
    st.dataframe(
        results["coverage_shifts"],
        hide_index=True,
        alt="Days far below the week before",
        column_order=["event_date", "event_name", "field_name", "present", "total", "before", "coverage", "after"],
        column_config={
            "event_date": "Date",
            "event_name": "Event",
            "field_name": "Field",
            "present": st.column_config.NumberColumn("Sent"),
            "total": st.column_config.NumberColumn("Events"),
            "before": st.column_config.NumberColumn("Week before", **percent),
            "coverage": st.column_config.NumberColumn("Coverage", **percent),
            "after": st.column_config.NumberColumn("Next day", **percent),
        },
    )
with volume:
    st.subheader("Days with no data")
    missing = pd.DataFrame(
        [(event, len(days)) for event, days in results["missing_days"].items() if days],
        columns=["Event", "Days with no data"],
    )
    st.dataframe(missing, hide_index=True, alt="Days each event did not arrive")
    st.subheader("Days far below the usual count")
    st.dataframe(
        results["low_days"],
        hide_index=True,
        alt="Days far below the usual count",
        column_order=["event_date", "weekday", "event_name", "event_count", "typical", "ratio"],
        column_config={
            "event_date": "Date",
            "weekday": "Weekday",
            "event_name": "Event",
            "event_count": st.column_config.NumberColumn("Count"),
            "typical": st.column_config.NumberColumn("Typical for weekday", format="%.1f"),
            "ratio": st.column_config.NumberColumn("Share of typical", format="percent"),
        },
    )
with types:
    st.subheader("Days with values of the wrong type")
    st.dataframe(
        results["type_mismatches"],
        hide_index=True,
        alt="Days with values of the wrong type",
        column_order=["event_date", "event_name", "field_name", "type", "wrong_type", "total", "text_values", "number_values", "empty_values"],
        column_config={
            "event_date": "Date",
            "event_name": "Event",
            "field_name": "Field",
            "type": "Planned type",
            "wrong_type": st.column_config.NumberColumn("Wrong type"),
            "total": st.column_config.NumberColumn("Values"),
            "text_values": st.column_config.NumberColumn("As text"),
            "number_values": st.column_config.NumberColumn("As number"),
            "empty_values": st.column_config.NumberColumn("Empty"),
        },
    )
with rules:
    st.subheader("Events that outnumber the event they require")
    st.dataframe(
        results["dependency_breaks"],
        hide_index=True,
        alt="Events that outnumber the event they require",
        column_order=["event_name", "event_count", "requires", "required_count", "reason"],
        column_config={
            "event_name": "Event",
            "event_count": st.column_config.NumberColumn("Count"),
            "requires": "Requires",
            "required_count": st.column_config.NumberColumn("Required event count"),
            "reason": "Why",
        },
    )
    st.subheader("Events where most records carry the same product count")
    st.dataframe(
        results["repeated_item_counts"],
        hide_index=True,
        alt="Events where most records carry the same product count",
        column_order=["event_name", "items_in_event", "events", "total", "share", "max_items"],
        column_config={
            "event_name": "Event",
            "items_in_event": st.column_config.NumberColumn("Products per record"),
            "events": st.column_config.NumberColumn("Records"),
            "total": st.column_config.NumberColumn("All records"),
            "share": st.column_config.NumberColumn("Share", format="percent"),
            "max_items": st.column_config.NumberColumn("Most products seen"),
        },
    )

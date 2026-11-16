"""Choose the data source and tracking plan to audit."""
from datetime import date, datetime

import pandas as pd
import streamlit as st

from bq import SETTINGS_PATH, load_settings
from plan import PLAN_DIR
from run_checks import DEMO

SETTINGS_TEMPLATE = """# Where the auditor reads data from. Change these to point at another GA4 export.
billing_project = "{billing_project}"
table = "{table}"
start_date = "{start_date}"
end_date = "{end_date}"

# Days with fewer records than this are skipped by the daily coverage check.
min_records_per_day = {min_records}
"""


REQUIRED_COLUMNS = {
    "events.csv": {"event_name", "status", "severity_if_missing", "used_in"},
    "event_fields.csv": {"event_name", "field_name", "location", "type", "required", "status", "measured_per", "used_in"},
    "event_dependencies.csv": {"event_name", "requires", "reason"},
    "calendar.csv": {"date", "name", "observed"},
}


def to_date(text: str) -> date:
    """Turn a GA4-style 20201101 date into a date the date picker understands."""
    return datetime.strptime(text, "%Y%m%d").date()


def forget_results() -> None:
    """Drop results and drafts made with the old settings or plan, so nothing stale is shown."""
    st.cache_data.clear()
    for key in ("results", "drafts"):
        st.session_state.pop(key, None)


st.title("Setup")
if DEMO:
    st.info("Demo: settings and the tracking plan are read-only. Clone the repo to audit your own GA4 export.", icon=":material/lock:")
settings = load_settings()

with st.form("settings"):
    st.subheader("Data source")
    table = st.text_input("GA4 export table", value=settings["table"], help="End with events_* to read every daily table.")
    billing_project = st.text_input("Billing project", value=settings["billing_project"], help="The Google Cloud project charged for the queries.")
    dates = st.date_input("Dates to audit", value=(to_date(settings["start_date"]), to_date(settings["end_date"])))
    min_records = st.number_input("Skip days with fewer records than", min_value=1, value=settings["min_records_per_day"])
    saved = st.form_submit_button("Save settings", type="primary", icon=":material/save:", disabled=DEMO)


if saved:
    if len(dates) != 2:
        st.error("Pick both a start and an end date.")
        st.stop()
    start, end = dates
    SETTINGS_PATH.write_text(
        SETTINGS_TEMPLATE.format(
            billing_project=billing_project.strip(),
            table=table.strip(),
            start_date=start.strftime("%Y%m%d"),
            end_date=end.strftime("%Y%m%d"),
            min_records=int(min_records),
        ),
        encoding="utf-8",
    )
    forget_results()
    st.success("Settings saved. Run the audit again on the Results page.")


st.subheader("Tracking plan")
plan_files = {
    "Events": "events.csv",
    "Fields": "event_fields.csv",
    "Dependencies": "event_dependencies.csv",
    "Holidays": "calendar.csv",
}
for tab, file_name in zip(st.tabs(list(plan_files)), plan_files.values(), strict=True):
    with tab:
        path = PLAN_DIR / file_name
        upload = None if DEMO else st.file_uploader(f"Replace {file_name}", type="csv", key=f"upload_{file_name}")
        if upload is not None:
            missing = REQUIRED_COLUMNS[file_name] - set(pd.read_csv(upload).columns)
            if missing:
                st.error(f"This file is missing columns: {', '.join(sorted(missing))}")
            elif st.button(f"Use the uploaded {file_name}", type="primary", key=f"use_{file_name}"):
                path.write_bytes(upload.getvalue())
                forget_results()
                st.success(f"{file_name} replaced. Run the audit again on the Results page.")
        if path.exists():
            st.dataframe(pd.read_csv(path), hide_index=True, alt=f"Tracking plan file {file_name}")
        else:
            st.info(f"No {file_name} yet.")

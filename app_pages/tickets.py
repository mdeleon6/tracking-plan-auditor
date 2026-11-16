"""Review the ticket drafts Claude writes from the results."""
import re

import streamlit as st

from ai_tickets import (
    OUTPUT_FOLDER,
    PREFIXES,
    describe_all,
    draft_ticket,
    find_severity,
    find_unsupported_numbers,
)
from run_checks import DEMO

LABELS = {
    "events": "Events",
    "field_gaps": "Field gaps",
    "type_mismatches": "Types",
    "missing_days": "Missing days",
    "low_days": "Low days",
    "dependency_breaks": "Dependencies",
    "repeated_item_counts": "Product counts",
}


def tidy(ticket: str) -> str:
    """Shrink the ticket's headings to fit in an expander and keep the header lines on separate lines."""
    ticket = re.sub(r"^## ", "#### ", ticket, flags=re.MULTILINE)
    ticket = re.sub(r"^# ", "### ", ticket, flags=re.MULTILINE)
    return ticket.replace("\n**", "  \n**")


st.title("Tickets")
if "results" not in st.session_state:
    st.info("Run the audit on the Results page first.")
    st.stop()

problems = describe_all(st.session_state["results"])
check = st.segmented_control("Check", list(LABELS), format_func=LABELS.get, default="events", required=True)
st.caption(f"{len(problems[check])} problems found by this check.")
drafts = st.session_state.setdefault("drafts", {})
for number, problem in enumerate(problems[check], start=1):
    key = f"{check}_{number}"
    with st.expander(f"Problem {number}"):
        st.code(problem, language=None, wrap_lines=True)
        if DEMO:
            saved = OUTPUT_FOLDER / f"{PREFIXES[check]}{number}.md"
            if saved.exists():
                drafts[key] = saved.read_text(encoding="utf-8")
            else:
                st.caption("No saved draft for this problem in the demo.")
        elif st.button("Draft ticket", key=f"draft_{key}", icon=":material/edit_note:"):
            with st.spinner("Claude is drafting the ticket..."):
                drafts[key] = draft_ticket(problem)
        if key in drafts:
            ticket = drafts[key]
            severity = find_severity(ticket)
            unsupported = find_unsupported_numbers(ticket, problem)
            with st.container(horizontal=True):
                if severity:
                    st.badge(f"Severity: {severity}", icon=":material/flag:", color="blue")
                else:
                    st.badge("Severity missing", icon=":material/error:", color="red")
                if unsupported:
                    st.badge(f"Check these numbers: {', '.join(sorted(unsupported))}", icon=":material/warning:", color="orange")
                else:
                    st.badge("Every number is in the check results", icon=":material/check:", color="green")
            with st.container(border=True):
                st.markdown(tidy(ticket))
            st.download_button(
                "Download ticket",
                data=ticket,
                file_name=f"{key}.md",
                mime="text/markdown",
                icon=":material/download:",
                key=f"download_{key}",
            )


"""Run the Tracking Plan Auditor app."""
import streamlit as st

st.set_page_config(page_title="Tracking Plan Auditor", page_icon=":material/fact_check:", layout="wide")

page = st.navigation([
    st.Page("app_pages/setup.py", title="Setup", icon=":material/settings:"),
    st.Page("app_pages/results.py", title="Results", icon=":material/analytics:"),
    st.Page("app_pages/tickets.py", title="Tickets", icon=":material/confirmation_number:"),
])
page.run()

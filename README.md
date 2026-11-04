# Tracking Plan Auditor

Catches broken analytics tracking before it reaches dashboards.

**Status:** In progress. Manual audit complete; automated auditor in development.

## The problem
When tracking is broken, incorrect data can be presented or unnecessary time can be spent on cleaning the data. The breaking of tracking happens silently, unless you are looking into it you may never see the issue. Through experience I have witnessed this myself, where until an audit was done the extent of how broken the tracking was would never have been realized. 

A feature can look like it failed, or a campaign can look like it worked, when the real cause is broken tracking.

## What I found so far
- `view_item_list`: fires on ~0.03% of category page loads (expected ~100%)
- `select_item`: only tracked from Nov 23, 2020, so earlier trends look like a fake spike

Full write-up: [findings/001-view-item-list.md](findings/001-view-item-list.md)

## Data
[Google's public GA4 sample](https://developers.google.com/analytics/bigquery/web-ecommerce-demo-dataset) from the Google Merchandise Store (Nov 2020 – Jan 2021), the only large public GA4 export. Same format as any company's GA4 data today.

## How it works (planned)
1. Compare the tracking plan with the live data: missing, extra or renamed events
2. Check required fields and data types
3. Spot unusual volume drops, comparing like with like (Saturdays with Saturdays)
4. AI explains each issue and drafts the ticket
5. Measured on planted bugs: how many it catches vs. false alarms

## Repo layout
- `queries/`: the SQL from the manual investigation
- `findings/`: audit tickets

## Tech
SQL (BigQuery), GA4, Python (planned), Claude API (planned)

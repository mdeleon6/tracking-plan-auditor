# Tracking Plan Auditor

Catches broken analytics tracking before it reaches dashboards.

**Status:** In progress. Manual audit complete; automated checks and AI ticket drafting working. UI and support for other data layouts planned.

## The problem
When tracking is broken, incorrect data can be presented or unnecessary time can be spent on cleaning the data. The breaking of tracking happens silently, unless you are looking into it you may never see the issue. Through experience I have witnessed this myself, where until an audit was done the extent of how broken the tracking was would never have been realized. 

A feature can look like it failed, or a campaign can look like it worked, when the real cause is broken tracking.

## What I found so far
- `view_item_list`: fires on ~0.03% of category page loads (expected ~100%)
- `select_item`: only tracked from Nov 23, 2020, so earlier trends look like a fake spike
- `purchase`: 7.9% of purchases have no `transaction_id`, rising to 82.3% from Jan 26–31, 2021 (cause not confirmed)
- `shipping_tier`: missing on 26.9% of purchases. Not sent until Nov 20, 2020, then missing on 5.6%, rising to 82.3% on Jan 26–31 alongside `transaction_id` (cause not confirmed)
- `add_to_cart`: no data on 18 of 92 days while purchases continued, and 90.7% of events list exactly 12 products, so the event alone doesn't show what was added (cause not confirmed)

**Found by the automated checks, beyond the manual audit**
- Dec 30, 2020: `transaction_id` and `purchase_revenue` on only 22 of 37 purchases, `shipping_tier` on 20
- Jan 24, 2021: add_to_cart `quantity` on only 39.5% of events for one day
- `purchase_revenue` missing on the same 450 purchases as `transaction_id`
- `refund`, `view_cart`, `add_to_wishlist` and `remove_from_cart` never arrive, though the plan lists them as active

Full write-ups: [`view_item_list`](findings/001-view-item-list.md), [`purchase`](findings/002-purchase-missing-transaction-id.md), [`shipping_tier`](findings/003-purchase-missing-shipping-tier.md), [`add_to_cart`](findings/004-add-to-cart-unreliable.md)

## Data
[Google's public GA4 sample](https://developers.google.com/analytics/bigquery/web-ecommerce-demo-dataset) from the Google Merchandise Store (Nov 2020 – Jan 2021), the only large public GA4 export. Same format as any company's GA4 data today.

## How it works
**Working now**
- Compares the tracking plan with the data: planned events that never arrive, events missing from the plan, and deprecated events still being sent. Each becomes a ticket, using the plan's severity rating (e.g. `refund` never arrived: High, because net revenue depends on it)
- Checks that required `event_params`, `items` and `ecommerce` fields, plus country, device and platform, are present on at least 99% of their events or products. The plan sets how each field is measured, so a field expected on one product per event (e.g. add_to_cart `quantity`) is checked per event
- Finds the days an event stopped arriving entirely
- Flags days far below an event's typical count for that weekday. Typical counts ignore days with no data, and some false alarms are expected around holidays
- Turns every check's results into problem descriptions and drafts a ticket for each with Claude (field gaps, missing days, low-volume days, planned events never received, event dependencies, repeated product counts). Claude must label any possible cause as unconfirmed and cannot calculate numbers. Days when many events drop together become one ticket
- Flags any number in a draft that isn't in the check results. It can't tell if a number is used in the wrong place, so a person reviews every draft
- Takes the severity of missing-day and never-received tickets from the tracking plan, where the plan owner rates how serious it is if that event stops arriving. If Claude disagrees, it keeps the plan's rating and adds a next step asking the owner to review it
- Tells Claude what each event and field feeds (from `used_in` columns in the plan, e.g. checkout conversion rate by country, or revenue by product), so it judges severity from facts instead of guessing
- Labels flagged days from a holiday calendar in the plan, including where each holiday is observed, since the store sells internationally. Claude treats holidays as context, not a cause
- Counts purchases missing two required fields together, so linked gaps are backed by evidence (e.g. the same 450 purchases lack transaction_id, value, tax, payment_type and purchase_revenue, and all of them also lack shipping_tier)
- Finds days when a required purchase field's coverage fell well below its normal level, grouped into stretches (e.g. transaction_id on 50 of 282 purchases on Jan 26–31). Found Dec 30, 2020, which the manual audit missed
- Finds lasting drops by comparing each day with the week before it, and says whether the next day recovered (e.g. add_to_cart `quantity` fell from 88.6% to 57.0% on Dec 9, 2020 and stayed low; Jan 24, 2021 was a one-day dip)
- Checks event dependencies from the plan (e.g. select_item can't outnumber view_item_list), using GA4 funnel defaults the analyst can edit. Works for web and apps alike
- Flags events where most records with products carry the same product count above 1 (e.g. 90.7% of add_to_cart records carry exactly 12, and none carry more). Single-product records are ignored, since one item is normal

**Planned**
- Build the field lists in the queries from the tracking plan, and run the daily and co-missing checks on every event, not only purchase and add_to_cart
- Warn when a required field never appears in the data, instead of reporting 0% coverage
- Move the check thresholds (e.g. 10 points, 7 days) into `settings.toml`
- A step-by-step guide for running the audit on your own GA4 export and tracking plan
- Check data types
- Extend planted bugs testing to the field checks
- A Streamlit app to run the checks and review Claude's drafts in one place
- Support for data stored as one table per event, not only GA4's single shared table

## How well it works
Tested by planting bugs in real daily counts (9 per size, 3 healthy events). The low-volume check caught every drop of 70% or more, 2 of 9 at 55%, and none at 40% or below. Small test; low-volume events are noisier.

## Repo layout
- `queries/manual/`: the SQL from the manual audit, fixed to the GA4 sample so the findings can be reproduced. 07 is missing because it became the field coverage check and moved to `queries/checks/`
- `queries/checks/`: the SQL the automated checks run. Reads the table and date range from `settings.toml`
- `findings/`: audit tickets and supporting results
- `tracking_plan/`: the plan the data is checked against
- `bq.py`: runs SQL files in BigQuery from Python
- `tests/`: pytest unit tests
- `planted_bugs.py`: tests the checks against bugs planted on purpose
- `ai_drafts/`: sample tickets drafted by Claude from real check results
- `settings.toml`: which GA4 export and date range to audit, and the project billed for queries
- `checks.py`: the checks, as pure functions with no BigQuery
- `run_checks.py`: runs the checks on BigQuery (the part a new data source replaces)
- `plan.py`: reads the tracking plan files
- `describe.py`: turns check results into problem descriptions for Claude
- `ai_tickets.py`: drafts tickets with Claude and flags unsupported numbers

## Tech
SQL (BigQuery), GA4, Python (pandas), pytest, Claude API

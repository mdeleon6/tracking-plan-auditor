# Tracking Plan Auditor

Catches broken analytics tracking before it reaches dashboards.

**Status:** In progress. Manual audit complete; first automated checks working, with more in development.

## The problem
When tracking is broken, incorrect data can be presented or unnecessary time can be spent on cleaning the data. The breaking of tracking happens silently, unless you are looking into it you may never see the issue. Through experience I have witnessed this myself, where until an audit was done the extent of how broken the tracking was would never have been realized. 

A feature can look like it failed, or a campaign can look like it worked, when the real cause is broken tracking.

## What I found so far
- `view_item_list`: fires on ~0.03% of category page loads (expected ~100%)
- `select_item`: only tracked from Nov 23, 2020, so earlier trends look like a fake spike
- `purchase`: 7.9% of purchases have no `transaction_id`, rising to 82.3% from Jan 26–31, 2021 (cause not confirmed)
- `shipping_tier`: missing on 26.9% of purchases. Not sent until Nov 20, 2020, then missing on 5.6%, rising to 82.3% on Jan 26–31 alongside `transaction_id` (cause not confirmed)
- `add_to_cart`: no data on 18 of 92 days while purchases continued, and 90.7% of events list exactly 12 products, so the event alone doesn't show what was added (cause not confirmed)

Full write-ups: [`view_item_list`](findings/001-view-item-list.md), [`purchase`](findings/002-purchase-missing-transaction-id.md), [`shipping_tier`](findings/003-purchase-missing-shipping-tier.md), [`add_to_cart`](findings/004-add-to-cart-unreliable.md)

## Data
[Google's public GA4 sample](https://developers.google.com/analytics/bigquery/web-ecommerce-demo-dataset) from the Google Merchandise Store (Nov 2020 – Jan 2021), the only large public GA4 export. Same format as any company's GA4 data today.

## How it works
**Working now**
- Compares the tracking plan with the data: planned events that never arrive, events missing from the plan, and deprecated events still being sent
- Checks that required `event_params`, `items` and `ecommerce` fields are present on at least 99% of their events or products
- Finds the days an event stopped arriving entirely
- Flags days far below an event's typical count for that weekday (expect some false alarms around holidays)

**Planned**
- Check data types
- Spot unusual volume drops, comparing like with like (Saturdays with Saturdays)
- AI explains each issue and drafts the ticket
- Extend planted bugs testing to the field checks

## How well it works
Tested by planting bugs in real daily counts (9 per size, 3 healthy events). The low-volume check caught every drop of 70% or more, 2 of 9 at 55%, and none at 40% or below. Small test; low-volume events are noisier.

## Repo layout
- `queries/`: the SQL from the manual investigation
- `findings/`: audit tickets and supporting results
- `tracking_plan/`: the plan the data is checked against
- `bq.py`: runs SQL files in BigQuery from Python
- `checks.py`: the automated checks
- `tests/`: pytest unit tests

## Tech
SQL (BigQuery), GA4, Python (pandas), pytest, Claude API (planned)

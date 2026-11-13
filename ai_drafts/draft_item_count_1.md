# view_item_list, add_to_cart, view_item and select_item mostly carry exactly 12 products per record, Nov 1 2020 to Jan 31 2021

**Event:** view_item_list, add_to_cart, view_item, select_item
**Found by:** · **Date found:** · **Severity:** High

## Description
An automated check looks for events where most records that include products carry the same number of products, when that number is above 1. Four events were flagged: view_item_list, add_to_cart, view_item and select_item. For each of them, most records with products carry exactly 12 products, and no record carries more than 12.

The tracking plan does not say how many products each event should carry. It is therefore not known whether 12 products per record is expected or a fault.

begin_checkout, purchase, select_promotion and view_promotion were also checked and were not flagged.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
- view_item_list: 43 of 43 records with products (100.0%) carry exactly 12 products. No record carries more than 12.
- add_to_cart: 53094 of 58543 records with products (90.7%) carry exactly 12 products. No record carries more than 12.
- view_item: 219633 of 241876 records with products (90.8%) carry exactly 12 products. No record carries more than 12.
- select_item: 25085 of 31006 records with products (80.9%) carry exactly 12 products. No record carries more than 12.
- Not flagged: begin_checkout, purchase, select_promotion, view_promotion.

The following information is missing from the check results:
- A day-by-day breakdown, so it is not known whether this happens across the whole period or starts on a particular date.
- Whether the 12 products in a record are distinct or repeated, and whether they match what the user actually viewed, selected or added.
- How the remaining records with products are distributed by product count.
- How many records of each event carry no products at all.

## Impact
According to the tracking plan, these events feed the following metrics:
- **add_to_cart:** add-to-cart rate, cart-to-purchase conversion rate, and the checkout funnel.
- **view_item:** product views, view-to-cart rate, and product performance by country and platform.
- **select_item:** product list click-through rate and item selection reporting.
- **view_item_list:** product list views and the list-to-product funnel step.

Severity is High because add_to_cart feeds add-to-cart rate and cart-to-purchase conversion rate, which are key conversion rates. Any metric that counts products rather than events, such as products added to cart, products viewed, or per-product performance, could be distorted if the 12 products do not reflect what users actually interacted with. Until it is confirmed what these products represent and how each metric is calculated, those numbers cannot be trusted. If it turns out that all of these metrics count events only and ignore products, the severity could be lowered.

There are some possible explanations, but none is confirmed by the check results:
- No record carries more than 12 products. This could mean products are being capped at 12, which would leave some records incomplete.
- Each event could be attaching a full list of products, rather than only the product the user interacted with.

These four events were flagged together. That does not by itself mean they share a cause.

## Suggested next steps
- Agree on and document in the tracking plan how many products each of these events is expected to carry.
- Review a sample of flagged records for each event. Check whether the 12 products are distinct, and whether they match the product the user viewed, selected or added.
- Confirm whether a limit of 12 products exists anywhere in how products are attached to events.
- Get a day-by-day breakdown of the share of records carrying exactly 12 products, to see when this began.
- Confirm whether add-to-cart rate, cart-to-purchase conversion rate, view-to-cart rate and product performance reports count events or count products. This shows which reported numbers are actually affected.

## Acceptance criteria
- The tracking plan states the expected number of products for view_item_list, add_to_cart, view_item and select_item.
- Records for these events carry product counts that match the tracking plan, and the products match what the user interacted with.
- The repeated product count check no longer flags these events. Alternatively, if 12 products is confirmed as correct for any of them, that is documented in the tracking plan.
- Each affected metric has a documented position on whether data from Nov 1, 2020 to Jan 31, 2021 can be used, and how.
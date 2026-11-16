# Most `view_item_list`, `add_to_cart`, `select_item` and `view_item` records carry exactly 12 products from Nov 1, 2020 to Jan 31, 2021

**Events:** view_item_list, add_to_cart, select_item, view_item
**Found by:** · **Date found:** · **Severity:** Medium

## Description
An automated check looks for events where most records with products carry the same number of products, above 1. Four events were flagged for Nov 1, 2020 to Jan 31, 2021. In each one, most records with products carry exactly 12 products, and no record carries more than 12.

The tracking plan does not say how many products each event should carry, so the check results cannot show whether 12 is correct. One possible explanation is that something limits the product list to 12. This is unconfirmed: the check results do not show why the count repeats.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
- **view_item_list:** 43 of 43 records with products (100.0%) carry exactly 12 products. No record carries more than 12.
- **add_to_cart:** 53094 of 58543 records with products (90.7%) carry exactly 12 products. No record carries more than 12.
- **select_item:** 25085 of 31006 records with products (80.9%) carry exactly 12 products. No record carries more than 12.
- **view_item:** 219633 of 241876 records with products (90.8%) carry exactly 12 products. No record carries more than 12.
- **Not flagged:** The check did not flag begin_checkout, purchase, select_promotion or view_promotion. This only means these events did not match this pattern. It does not show that their product data is complete or correct.
- **Missing details:**
  - The check results do not say how many products the remaining records carry.
  - The check results do not say whether the 12 products are the same products from record to record.
  - The check results do not give a breakdown by day.

## Impact
According to the tracking plan, the flagged events feed these reports:
- **view_item_list:** product list views and the list-to-product funnel step.
- **add_to_cart:** add-to-cart rate, cart-to-purchase conversion rate and the checkout funnel.
- **select_item:** product list click-through rate and item selection reporting.
- **view_item:** product views, view-to-cart rate and product performance by country and platform.

Any report that counts or breaks down by product could be distorted if the 12 products do not reflect what users actually saw, selected or added to the cart. Product performance by country and platform and item selection reporting are examples.

**Why Medium rather than High:** The flagged pattern is in the number of products per record, not in whether events were received. Purchase, which carries revenue, orders and units sold, was not flagged by this check. Those key numbers do not obviously depend on the flagged data, so the affected reporting is the product-level breakdowns.

However, the check results do not show how add-to-cart rate, cart-to-purchase conversion rate or view-to-cart rate are calculated. If any of these rates are built from product counts rather than event counts, a key conversion rate would be affected and this ticket should be raised to High. This has not been confirmed.

## Suggested next steps
- **Expected product counts:** Ask the tracking plan owner how many products each of the four events is meant to carry. Add that expectation to the tracking plan.
- **Possible limit at 12:** Check whether the tracking implementation limits product lists to 12. This is a possible explanation only.
- **Which products are sent:** For a sample of flagged records, compare the 12 products sent with what the user actually viewed, selected or added to the cart. Check whether the same 12 products repeat across records.
- **Remaining records:** Review the add_to_cart, select_item and view_item records that do not carry 12 products. The check results do not describe them.
- **Rate calculations:** Confirm whether add-to-cart rate, cart-to-purchase conversion rate and view-to-cart rate count events or products. Raise severity to High if they count products.
- **Daily pattern:** Run a day-by-day view of the product count per record to see whether the pattern covers the whole period or starts at a certain point.

## Acceptance criteria
- The tracking plan states the expected number of products for view_item_list, add_to_cart, select_item and view_item.
- The products sent on each of these events match what the user actually viewed, selected or added to the cart, with no limit unless the tracking plan defines one.
- The repeated product counts check no longer flags these four events, or any remaining flag is explained by the documented expected product count.
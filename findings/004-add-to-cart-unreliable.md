# 90.7% of `add_to_cart` events carry exactly 12 products, and 18 days have no data (Nov 1 2020 - Jan 31 2021)

**Event:** add_to_cart
**Found by:** Martino DeLeon · **Date found:** 2026-11-06 · **Severity:** High

## Description
`add_to_cart` cannot currently be trusted, for three reasons. The event has no data on 18 of the 92 days, even though purchases continued on those days. Most events list exactly 12 products, so the event alone does not show which product was added. `quantity` appears to mark the product that was added, but it is present on only 63.6% of events and drops sharply around Dec 8-9, 2020.

These problems affect the same event but happen on different dates, so they may not share a cause. No cause has been confirmed, and the obfuscated sample data may be a factor.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
**Missing days**
- No `add_to_cart` events on 18 of 92 days: Nov 2-15 and Nov 21-24, 2020.
- 1,071 of 5,692 purchases (18.8%) happened on those 18 days.
- Volume is also very low next to the gaps: 4 events on Nov 1 and 15 events on Nov 20.

**Fixed list of 12 products**
- 58,543 events carry 667,426 products, an average of 11.4 per event.
- 53,094 events (90.7%) carry exactly 12 products. 1,849 (3.2%) carry 1. None carry more than 12.
- Other browsing events show the same pattern: `view_item` 90.8%, `select_item` 80.9%, and `view_item_list` 43 of 43 events with items.
- Checkout events do not: `begin_checkout` reaches 31 products and `purchase` reaches 30, and very few have exactly 12.

**`quantity` marker**
- 37,260 events (63.6%) have exactly one product with `quantity`. 21,283 (36.4%) have none. No event has more than one.
- Share of events with `quantity`:
  - Nov 16-20, 2020: 99.4% (1,435 of 1,443)
  - Nov 25 - Dec 7, 2020: 89.1% (13,517 of 15,172)
  - Dec 8, 2020: 83.1% (1,475 of 1,775)
  - Dec 9, 2020 - Jan 31, 2021: 51.9% (20,830 of 40,149)

**What is working**
- `item_id`, `item_name`, `item_category` and `price` are each filled in on 99.98% of products.
- No event has an empty `items` list.

**Queries**
- [`queries/10_items_coverage.sql`](../queries/10_items_coverage.sql)
- [`queries/11_add_to_cart_empty_items.sql`](../queries/11_add_to_cart_empty_items.sql)
- [`queries/12_items_per_add_to_cart.sql`](../queries/12_items_per_add_to_cart.sql)
- [`queries/13_items_by_event.sql`](../queries/13_items_by_event.sql)
- [`queries/14_quantity_per_add_to_cart.sql`](../queries/14_quantity_per_add_to_cart.sql)
- [`queries/15_quantity_by_day.sql`](../queries/15_quantity_by_day.sql)

## Impact
Cart-to-purchase rates will be wrong for November. Purchases were recorded on the 18 missing days but cart activity was not, including the days just before Black Friday.

Product-level cart reporting is also unreliable. Counting every listed product would overstate products added by about 11 times, and any "most added product" report could credit products the customer never added. If `quantity` does mark the added product, 36.4% of events still cannot show what was added.

These numbers feed decisions on merchandising and the checkout funnel, which is why this is High.

## Suggested next steps
- Find out why `add_to_cart` stopped on Nov 2-15 and Nov 21-24, 2020. Check for tracking or site releases around those dates.
- Confirm what the 12-product list is, and why browsing events carry it. One possibility is a product grid on the page.
- Confirm that `quantity` marks the product that was added, using a test purchase or the tracking code.
- Find out what changed around Dec 8-9, 2020, when `quantity` dropped from about 89% to about 52%.
- Follow `add_to_cart` events within a single visit, using `ga_session_id` with `user_pseudo_id`, to see how the product list changes as someone shops.
- Check whether the obfuscated sample data is causing any of this, by comparing with unobfuscated data if it is available.

Each of these can become its own ticket if the fixes turn out to be separate.

## Acceptance criteria
- `add_to_cart` is recorded on every day the store takes purchases.
- Each event identifies the product that was added, either by listing only that product or by marking it on 100% of events.
- Until this is fixed, cart analysis starts from Nov 25, 2020, the first day of continuous data. Any analysis that relies on `quantity` notes the drop from Dec 9, 2020.
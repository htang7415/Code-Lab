# 122.Best Time to Buy and Sell Stock II (DP)

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Find the maximum profit when you may complete as many buy/sell transactions as you want.

## Recognition Cues

- You may buy and sell multiple times, but cannot hold multiple stocks at once.
- Daily decisions can be modeled as "holding" or "not holding".
- This is a small-state DP over time.

## Baseline Idea

Try every possible set of transaction boundaries recursively. That works, but it explodes combinatorially.

## Core Insight

Track two states for each day:
- `cash`: best profit when not holding a stock
- `hold`: best profit when holding a stock

Each new price updates those states by either keeping the old state or performing a buy/sell transition.

## Invariant / State

- `cash` is the best profit after processing the day while holding no stock.
- `hold` is the best profit after processing the day while holding one stock.

## Walkthrough

For `[7, 1, 5, 3, 6, 4]`:
- Buying at `1` improves the hold state.
- Selling at `5` improves cash.
- Buying again at `3` improves hold relative to the new cash.
- Selling at `6` gives the final profit `7`.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Edge Cases

- Empty input
- One day
- Prices always decreasing
- Prices always increasing

## Common Mistakes

- Mixing this up with the one-transaction stock problem
- Updating `hold` using the new `cash` from the same day instead of the previous one
- Forgetting that you cannot hold more than one stock

## Pattern Transfer

- Small-state DP
- Stock trading state machines
- 121 and 123 stock variants

## Self-Check

- What do `cash` and `hold` mean?
- Why do we need the previous `cash` value when updating `hold`?
- How does unlimited trading change the transition logic from problem 121?

## Function

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/122-best-time-to-buy-and-sell-stock-ii-dp/python -q
```

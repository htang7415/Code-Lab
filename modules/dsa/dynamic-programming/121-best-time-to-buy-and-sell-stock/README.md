# 121.Best Time to Buy and Sell Stock

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Find the maximum profit from exactly one buy and one later sell.

## Recognition Cues

- Only one transaction is allowed.
- Profit depends on the best earlier buy price for each day.
- A running minimum captures the only state you need.

## Baseline Idea

Check every possible buy day against every later sell day and keep the best profit. That works, but it is `O(n^2)`.

## Core Insight

As you scan from left to right, track the cheapest price seen so far. For each current price, the best profit selling today is `price - min_price`, so update the global best in one pass.

## Invariant / State

- `min_price` is the smallest price seen before or at the current day.
- `best` is the maximum profit achievable so far with one transaction.

## Walkthrough

For `[7, 1, 5, 3, 6, 4]`:
- See `7`, so `min_price = 7`.
- See `1`, so update `min_price = 1`.
- See `5`, so profit `= 4`.
- See `6`, so profit `= 5`, which becomes the best answer.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Edge Cases

- Empty input
- One day
- Prices always decreasing

## Common Mistakes

- Selling before buying
- Resetting the best profit incorrectly
- Treating this like the unlimited-transactions version

## Pattern Transfer

- Running minimum / maximum tracking
- 122.Best Time to Buy and Sell Stock II
- One-pass array optimization

## Self-Check

- Why is the best buy for day `i` always the minimum earlier price?
- Why can the answer be found in one pass?
- What should be returned when prices always fall?

## Function

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/121-best-time-to-buy-and-sell-stock/python -q
```

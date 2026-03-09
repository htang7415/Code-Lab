# 123.Best Time to Buy and Sell Stock III

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Find the maximum profit with at most two stock transactions.

## Recognition Cues

- The number of transactions is limited.
- Each transaction has a buy state and a sell state.
- A small fixed number of states can encode the best answer so far.

## Baseline Idea

Enumerate all possible first and second transactions and keep the best combined profit. That works conceptually, but it repeats too much work.

## Core Insight

Track four rolling states:
- `buy1`: best balance after first buy
- `sell1`: best profit after first sell
- `buy2`: best balance after second buy
- `sell2`: best profit after second sell

Each price updates the best way to be in each state.

## Invariant / State

- Each state represents the best possible profit balance after a specific stage of the two-transaction process.

## Walkthrough

For `[3, 3, 5, 0, 0, 3, 1, 4]`:
- The first transaction can buy low and sell at `5`.
- The second transaction can buy again at `0` and sell at `4`.
- The rolling states accumulate the best combination, giving `6`.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Edge Cases

- Empty input
- One day
- No profitable transaction
- Best answer uses only one transaction

## Common Mistakes

- Resetting second-transaction states incorrectly
- Forgetting that the second buy depends on the profit from the first sell
- Solving the unlimited-transactions version by mistake

## Pattern Transfer

- Stock DP with bounded transactions
- 121, 122, 188 stock variants
- Finite-state DP

## Self-Check

- What does each of the four states mean?
- Why does `buy2` depend on `sell1`?
- When can the best answer use fewer than two transactions?

## Function

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/123-best-time-to-buy-and-sell-stock-iii/python -q
```

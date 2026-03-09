# 1049.Last Stone Weight II

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Split the stones into two groups so the remaining weight difference is as small as possible.

## Recognition Cues

- The final smash result depends only on how the stones are partitioned.
- Minimizing the leftover is the same as balancing two piles as closely as possible.
- This is a 0/1 knapsack problem on half of the total sum.

## Baseline Idea

Try every partition of the stones into two groups and track the smallest difference. That works, but it is exponential.

## Core Insight

If the total sum is `S`, then you want one pile as close as possible to `S // 2`. A 0/1 knapsack DP can find the largest achievable pile sum up to that target, and the answer is `S - 2 * best`.

## Invariant / State

- `dp[t]` is the largest achievable pile sum not exceeding capacity `t`.

## Walkthrough

For `[2, 7, 4, 1, 8, 1]`:
- Total is `23`, so target is `11`.
- DP finds the best achievable sum up to `11`.
- If one pile reaches `11`, the other is `12`, so the leftover is `1`.

## Complexity

- Time: `O(n * target)`
- Space: `O(target)`

## Edge Cases

- One stone
- Perfectly balanced partition
- Large stone that dominates the total

## Common Mistakes

- Thinking the smash order matters after the partition insight
- Iterating capacities forward instead of backward for 0/1 knapsack
- Forgetting to target only half of the total sum

## Pattern Transfer

- 0/1 knapsack
- Partition equal subset style problems
- Minimize difference by maximizing half-sum

## Self-Check

- Why can the problem be reduced to partitioning?
- Why is `S // 2` the only target range that matters?
- Why must the capacity loop go backward?

## Function

```python
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/1049-last-stone-weight-ii/python -q
```

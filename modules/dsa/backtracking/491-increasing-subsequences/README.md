# 491.Increasing Subsequences

> Track: `dsa` | Topic: `backtracking`

## Problem in One Line

Return all distinct non-decreasing subsequences of length at least `2`.

## Recognition Cues

- You need subsequences, not contiguous subarrays.
- Duplicate values can create repeated subsequences.
- Monotonic validity depends on the last chosen value.

## Baseline Idea

Generate all subsequences of length at least two and deduplicate them afterward. That works, but it explores many duplicate branches.

## Core Insight

Backtrack by index, allow only values that are at least the last chosen one, and use a local `used` set at each depth to avoid starting duplicate branches from equal values.

## Invariant / State

- `path` is the current subsequence.
- `used` at one recursion depth records which values have already been chosen as the next element at that depth.

## Walkthrough

For `[4, 6, 7, 7]`:
- Build `[4, 6]`, `[4, 6, 7]`, `[4, 6, 7, 7]`.
- A local `used` set prevents duplicate branches starting from the second `7` at the same depth.

## Complexity

- Time: exponential in the number of subsequences
- Space: `O(n)` recursion depth, excluding the output

## Edge Cases

- Strictly decreasing input
- All equal values
- Duplicate values that can extend many valid subsequences

## Common Mistakes

- Using one global deduplication set instead of one per depth
- Allowing decreasing extensions
- Recording subsequences of length `1`

## Pattern Transfer

- 90.Subsets II
- 47.Permutations II
- Backtracking with local-depth deduplication

## Self-Check

- Why is the `used` set local to each depth?
- Why are equal values allowed in the subsequence?
- When does a path become valid enough to record?

## Function

```python
class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
```

## Run tests

```bash
pytest modules/dsa/backtracking/491-increasing-subsequences/python -q
```

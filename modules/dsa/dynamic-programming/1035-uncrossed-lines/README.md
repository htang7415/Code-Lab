# 1035.Uncrossed Lines

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Find the maximum number of matching pairs you can connect between two arrays without crossings.

## Recognition Cues

- The order of matches matters.
- Crossing is forbidden, so matches must preserve relative order.
- This is the same structure as longest common subsequence on arrays.

## Baseline Idea

Try all possible match choices recursively and keep the best valid set. That works conceptually, but the overlapping subproblems make it too slow.

## Core Insight

Let `dp[i][j]` be the best answer using the first `i` values of `nums1` and the first `j` values of `nums2`. If the last values match, extend the best smaller match set; otherwise, skip one side and take the better answer.

## Invariant / State

- `dp[i][j]` stores the best non-crossing match count for the prefixes `nums1[:i]` and `nums2[:j]`.

## Walkthrough

For `[1, 4, 2]` and `[1, 2, 4]`:
- `1` matches `1`, so one line is possible.
- `4` and `2` cannot both match in crossing order.
- The best valid answer is `2`.

## Complexity

- Time: `O(mn)`
- Space: `O(mn)`

## Edge Cases

- One empty array
- No matching values
- Repeated values with multiple possible alignments

## Common Mistakes

- Treating it like set intersection and ignoring order
- Forgetting that crossings are prevented by preserving subsequence order
- Using the wrong prefix interpretation for `dp[i][j]`

## Pattern Transfer

- 1143.Longest Common Subsequence
- Sequence alignment DP
- Grid DP over two inputs

## Self-Check

- Why is this equivalent to LCS?
- What does `dp[i][j]` mean exactly?
- When values differ, why do we take `max(dp[i-1][j], dp[i][j-1])`?

## Function

```python
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/1035-uncrossed-lines/python -q
```

# 1143.Longest Common Subsequence

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Find the length of the longest subsequence common to two strings.

## Recognition Cues

- Order must be preserved, but characters do not need to be contiguous.
- Two input sequences suggest a 2D DP grid.
- Matching characters extend a smaller subproblem.

## Baseline Idea

Try every subsequence of one string and check whether it appears in the other. That works in theory, but it is far too slow.

## Core Insight

Let `dp[i][j]` be the LCS length for `text1[:i]` and `text2[:j]`. Matching last characters extend the diagonal answer; otherwise, skip one character from one side and keep the better result.

## Invariant / State

- `dp[i][j]` stores the best subsequence length for the two prefixes ending before `i` and `j`.

## Walkthrough

For `"abcde"` and `"ace"`:
- `a` matches `a`, so start with `1`.
- `c` matches later and extends the answer to `2`.
- `e` matches later and extends it to `3`.

## Complexity

- Time: `O(mn)`
- Space: `O(mn)`

## Edge Cases

- One empty string
- No common characters
- Repeated characters

## Common Mistakes

- Confusing subsequence with substring
- Using the wrong meaning for `dp[i][j]`
- Forgetting the extra zero row and zero column for empty prefixes

## Pattern Transfer

- 1035.Uncrossed Lines
- 72.Edit Distance
- Two-sequence DP tables

## Self-Check

- Why is subsequence easier than substring here?
- What does the diagonal cell represent when characters match?
- Why do we take the max of top and left when they do not match?

## Function

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/1143-longest-common-subsequence/python -q
```

# 115.Distinct Subsequences

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Count how many distinct subsequences of `s` equal `t`.

## Recognition Cues

- The task asks for a count, not a yes/no answer.
- Characters can be skipped in `s`, but the relative order must stay.
- DP over prefixes avoids recomputing many repeated counting branches.

## Baseline Idea

Recursively choose whether to use or skip each character of `s`. That captures the structure, but it repeats the same subproblems many times.

## Core Insight

Use DP where matching a character can extend all ways that formed the previous prefix of `t`, and skipping a character keeps existing counts. The 1D optimization works by iterating `t` backward so each character of `s` is used only once per step.

## Invariant / State

- `dp[j]` is the number of ways to form `t[:j]` using the processed prefix of `s`.
- `dp[0]` is always `1` because the empty string can always be formed.

## Walkthrough

For `s = "rabbbit"` and `t = "rabbit"`:
- Each matching `b` can either be used or skipped.
- DP accumulates the different valid ways to choose two of the three `b` characters.
- The final count is `3`.

## Complexity

- Time: `O(len(s) * len(t))`
- Space: `O(len(t))`

## Edge Cases

- Empty target string
- Target longer than source
- Many repeated characters creating multiple counts

## Common Mistakes

- Using forward iteration on `t` and accidentally reusing the same `s` character multiple times
- Forgetting that the empty target has exactly one valid subsequence
- Treating the problem like LCS length instead of count DP

## Pattern Transfer

- Count-based subsequence DP
- 392.Is Subsequence
- Backward 1D DP updates

## Self-Check

- Why is `dp[0] = 1`?
- Why must the loop over `t` go backward?
- What does matching one new character contribute to the count?

## Function

```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/115-distinct-subsequences/python -q
```

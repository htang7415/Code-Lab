# 139.Word Break

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Decide whether the string can be segmented into words from the dictionary.

## Recognition Cues

- The decision is over prefixes of the string.
- Valid earlier cuts can enable later ones.
- A boolean DP over positions is a natural fit.

## Baseline Idea

Try every possible split recursively and check whether both parts work. That works, but it repeats the same suffix checks many times.

## Core Insight

Let `dp[i]` mean whether `s[:i]` can be segmented. For each end position `i`, check earlier cut positions `j`; if `dp[j]` is true and `s[j:i]` is a dictionary word, then `dp[i]` is true.

## Invariant / State

- `dp[i]` answers whether the prefix ending before index `i` is segmentable.

## Walkthrough

For `"leetcode"` with `["leet", "code"]`:
- `dp[4]` becomes true because `"leet"` is a word and `dp[0]` is true.
- `dp[8]` becomes true because `"code"` is a word and `dp[4]` is true.
- The full string is segmentable.

## Complexity

- Time: `O(n^2)` plus substring lookup cost
- Space: `O(n)` plus the dictionary set

## Edge Cases

- Empty string
- No valid segmentation
- Multiple valid segmentations
- Repeated prefix words

## Common Mistakes

- Forgetting to seed `dp[0] = True`
- Checking words without verifying the earlier prefix is valid
- Using a list instead of a set for repeated dictionary lookups

## Pattern Transfer

- Prefix DP
- String segmentation problems
- Boolean reachability over positions

## Self-Check

- What does `dp[i]` mean?
- Why is `dp[0]` true?
- What condition must a cut position `j` satisfy to make `dp[i]` true?

## Function

```python
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/139-word-break/python -q
```

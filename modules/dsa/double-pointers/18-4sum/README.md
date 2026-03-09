# 18.4Sum

> Track: `dsa` | Topic: `double-pointers`

## Problem in One Line

Return all unique quadruplets whose values sum to `target`.

## Recognition Cues

- The problem asks for unique combinations of four numbers.
- Sorting helps manage duplicates.
- After fixing two values, the rest becomes a two-pointer search on a sorted suffix.

## Baseline Idea

Try every quadruplet with four nested loops and deduplicate the result. This works, but it is too slow at `O(n^4)`.

## Core Insight

Sort the array, fix the first two numbers, then use left and right pointers to search for the remaining pair. Because the array is sorted, pointer moves increase or decrease the sum in a predictable way, and duplicates can be skipped at every level.

## Invariant / State

- For fixed indices `i` and `j`, the pointers search only in the range to the right of `j`.
- Duplicate anchors and duplicate pointer values are skipped so each quadruplet appears once.

## Walkthrough

For `[1, 0, -1, 0, -2, 2]` with `target = 0`:
- Sort to `[-2, -1, 0, 0, 1, 2]`.
- Fix `-2`, then `-1`, and search with pointers.
- Repeat for the next second anchor values.
- Every time the sum matches `0`, record the quadruplet and skip repeated values.

## Complexity

- Time: `O(n^3)` after sorting
- Space: `O(1)` extra space, ignoring output

## Edge Cases

- Fewer than 4 numbers
- No valid quadruplet
- Many duplicate values

## Common Mistakes

- Forgetting to skip duplicates for the first or second anchor
- Moving the wrong pointer after comparing the sum to `target`
- Returning the same quadruplet multiple times

## Pattern Transfer

- 15.3Sum
- Sorted `k`-sum problems
- Two-pointer search after fixing anchors

## Self-Check

- Why is this one dimension harder than `3Sum`?
- Which loops or pointers need duplicate skipping?
- After fixing two numbers, what problem are the pointers solving?

## Function

```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
```

## Run tests

```bash
pytest modules/dsa/double-pointers/18-4sum/python -q
```

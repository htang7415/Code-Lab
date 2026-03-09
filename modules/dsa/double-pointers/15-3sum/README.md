# 15.3Sum

> Track: `dsa` | Topic: `double-pointers`

## Problem in One Line

Return all unique triplets whose values sum to `0`.

## Recognition Cues

- The problem asks for unique triplets, not just one answer.
- Sorting can group duplicates and make pointer movement meaningful.
- After fixing one value, the remaining task looks like `2Sum` on a sorted array.

## Baseline Idea

Try every triple with three nested loops and deduplicate at the end. This works, but it costs `O(n^3)` time.

## Core Insight

Sort the array, fix one number, then use a left pointer and a right pointer to search for the remaining two numbers. Because the array is sorted, moving the pointers adjusts the sum in a predictable way, and duplicate values can be skipped cleanly.

## Invariant / State

- For a fixed index `i`, the pointers search only in the sorted range to the right of `i`.
- Every recorded triplet is unique because repeated anchor and pointer values are skipped.

## Walkthrough

For `[-1, 0, 1, 2, -1, -4]`:
- Sort to `[-4, -1, -1, 0, 1, 2]`.
- Fix `-1` at index `1`.
- Move left and right pointers inward until the sum hits `0`.
- Skip duplicate `-1` anchors and duplicate pointer values so each triplet is recorded once.

## Complexity

- Time: `O(n^2)` after sorting
- Space: `O(1)` extra space, ignoring output

## Edge Cases

- Fewer than 3 numbers
- No valid triplet
- Many duplicates like all zeros

## Common Mistakes

- Forgetting to sort before using two pointers
- Returning duplicate triplets
- Moving only one pointer after finding a valid triplet

## Pattern Transfer

- 18.4Sum
- 167.Two Sum II
- General `k`-sum reduction by sorting and fixing values

## Self-Check

- Why does sorting make two-pointer movement valid?
- Why do duplicates need to be skipped at both the anchor and pointer levels?
- After fixing one value, what smaller problem remains?

## Function

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
```

## Run tests

```bash
pytest modules/dsa/double-pointers/15-3sum/python -q
```

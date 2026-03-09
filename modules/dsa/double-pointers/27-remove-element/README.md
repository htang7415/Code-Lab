# 27.Remove Element

> Track: `dsa` | Topic: `double-pointers`

## Problem in One Line

Remove all instances of `val` in place and return the new logical length.

## Recognition Cues

- The array can be modified in place.
- The order of kept elements may stay compacted at the front.
- A read pointer and a write pointer fit naturally.

## Baseline Idea

Create a new array with only the kept values, then copy it back. That works, but it uses extra space.

## Core Insight

Use a fast pointer to scan every value and a slow pointer to mark the next write position for values that should be kept. Every non-`val` number is copied forward exactly once.

## Invariant / State

- `nums[:slow]` always contains the kept values seen so far.
- `fast` scans each original position exactly once.

## Walkthrough

For `nums = [3, 2, 2, 3]` and `val = 3`:
- Skip the first `3`.
- Copy `2` to position `0`.
- Copy the next `2` to position `1`.
- Skip the final `3`.
- Return `2` because the kept prefix is `[2, 2]`.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Edge Cases

- Empty array
- No value matches `val`
- Every value matches `val`

## Common Mistakes

- Forgetting that only the first `k` elements matter after the call
- Advancing the write pointer even when the value should be removed
- Checking the full mutated array instead of `nums[:k]`

## Pattern Transfer

- Stable in-place filtering
- 26.Remove Duplicates from Sorted Array
- Partitioning with read/write pointers

## Self-Check

- What does the prefix `nums[:slow]` represent during the scan?
- Why is it safe to overwrite earlier positions?
- Why do the values after index `k - 1` not matter?

## Function

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
```

## Run tests

```bash
pytest modules/dsa/double-pointers/27-remove-element/python -q
```

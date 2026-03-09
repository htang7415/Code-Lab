# 347.Top K Frequent Elements

> Track: `dsa` | Topic: `stack-and-queue`

## Problem in One Line

Return the `k` values that appear most often in the array.

## Recognition Cues

- Frequency counting is the first step.
- You need the top `k`, not a fully sorted order of everything.
- Bucket grouping by frequency avoids sorting every distinct value.

## Baseline Idea

Count the values, sort all `(value, frequency)` pairs by frequency, then take the first `k`. That works, but it sorts more than needed.

## Core Insight

After counting frequencies, place each value into a bucket indexed by its frequency. Then scan the buckets from high frequency to low until `k` elements have been collected.

## Invariant / State

- Bucket `f` contains exactly the values that appear `f` times.
- Scanning buckets from the end visits frequencies in descending order.

## Walkthrough

For `[1, 1, 1, 2, 2, 3]` with `k = 2`:
- Count frequencies: `1 -> 3`, `2 -> 2`, `3 -> 1`.
- Put `1` in bucket `3`, `2` in bucket `2`, `3` in bucket `1`.
- Scan buckets from high to low and stop after taking `1` and `2`.

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Edge Cases

- One element
- `k` equals the number of distinct values
- Negative numbers

## Common Mistakes

- Sorting all values when bucket grouping is enough
- Building too few buckets
- Forgetting that the result order within the top `k` does not matter here

## Pattern Transfer

- Frequency counting with `Counter`
- Bucket-sort style grouping
- Top-`k` selection problems

## Self-Check

- Why are `len(nums) + 1` buckets enough?
- Why does scanning buckets backward produce the most frequent values first?
- When does result order matter, and when does it not?

## Function

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
```

## Run tests

```bash
pytest modules/dsa/stack-and-queue/347-top-k-frequent-elements/python -q
```

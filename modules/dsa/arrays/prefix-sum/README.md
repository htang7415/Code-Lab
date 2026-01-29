# Prefix Sum

> Track: `dsa` | Topic: `arrays`

## Concept

A **prefix sum** (cumulative sum) array stores running totals so that any
subarray sum can be computed in O(1) after O(n) preprocessing.

Given an array `a` of length `n`, the prefix sum array `p` is defined as:

```
p[0] = 0
p[i] = a[0] + a[1] + ... + a[i-1]
```

The sum of elements from index `l` to `r` (inclusive) is `p[r+1] - p[l]`.

## Key points

- Build time: O(n), query time: O(1)
- Useful for range sum queries, subarray sum problems, and difference arrays
- Can be extended to 2D grids (2D prefix sums)

## Run tests

```bash
pytest modules/dsa/arrays/prefix-sum/python -q
```

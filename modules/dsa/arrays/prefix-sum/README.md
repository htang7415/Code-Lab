# Prefix Sum

> Track: `dsa` | Topic: `arrays`

## Concept

A **prefix sum** (cumulative sum) array stores running totals so that any
subarray sum can be computed in **O(1)** after **O(n)** preprocessing.

Use cases: range sum queries, subarray sum problems, difference arrays,
and 2D grid prefix sums.

## Math

$$\text{Given an array \texttt{a} of length \texttt{n}, the prefix sum array \texttt{p} of length \texttt{n+1}:}$$

```
p[0] = 0
p[i] = a[0] + a[1] + ... + a[i-1]    for i = 1..n
```

$$\text{Sum of elements from index \texttt{l} to \texttt{r} (inclusive):}$$

```
sum(l, r) = p[r+1] - p[l]
```

- $\text{Build time: **O(n)**}$
- $\text{Query time: **O(1)**}$

## Function

```python
def prefix_sum(arr: list[int]) -> list[int]
```

- `arr` — input array of integers
- Returns — prefix sum array of length `len(arr) + 1`
- `result[0] = 0`, `result[i] = sum(arr[0..i-1])`

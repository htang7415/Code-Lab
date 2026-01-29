"""Prefix sum — build and query range sums in O(1)."""

from typing import List


def build_prefix_sum(arr: List[int]) -> List[int]:
    """Return a prefix sum array of length len(arr)+1.

    prefix[i] = sum of arr[0..i-1], with prefix[0] = 0.
    """
    prefix = [0] * (len(arr) + 1)
    for i, val in enumerate(arr):
        prefix[i + 1] = prefix[i] + val
    return prefix


def range_sum(prefix: List[int], left: int, right: int) -> int:
    """Return sum of the original array from index left to right (inclusive).

    Requires the prefix sum array from build_prefix_sum.
    """
    return prefix[right + 1] - prefix[left]

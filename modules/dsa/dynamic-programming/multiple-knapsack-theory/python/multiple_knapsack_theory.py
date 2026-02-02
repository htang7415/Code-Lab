from typing import List

class Solution:
    def multipleKnapsack(self, weights: List[int], values: List[int], counts: List[int], capacity: int) -> int:
        items: list[tuple[int, int]] = []
        for w, v, c in zip(weights, values, counts):
            for _ in range(c):
                items.append((w, v))
        dp = [0] * (capacity + 1)
        for w, v in items:
            for c in range(capacity, w - 1, -1):
                dp[c] = max(dp[c], dp[c - w] + v)
        return dp[capacity]

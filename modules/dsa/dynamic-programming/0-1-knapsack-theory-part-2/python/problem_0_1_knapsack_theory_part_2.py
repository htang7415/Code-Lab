from typing import List

class Solution:
    def knapSack(self, weights: List[int], values: List[int], capacity: int) -> int:
        dp = [0] * (capacity + 1)
        for w, v in zip(weights, values):
            for c in range(capacity, w - 1, -1):
                dp[c] = max(dp[c], dp[c - w] + v)
        return dp[capacity]

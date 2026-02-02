from typing import List

class Solution:
    def completeKnapsack(self, weights: List[int], values: List[int], capacity: int) -> int:
        dp = [0] * (capacity + 1)
        for w, v in zip(weights, values):
            for c in range(w, capacity + 1):
                dp[c] = max(dp[c], dp[c - w] + v)
        return dp[capacity]

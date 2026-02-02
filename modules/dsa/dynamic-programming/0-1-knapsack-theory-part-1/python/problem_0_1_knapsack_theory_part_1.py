from typing import List

class Solution:
    def knapSack(self, weights: List[int], values: List[int], capacity: int) -> int:
        n = len(weights)
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            w = weights[i - 1]
            v = values[i - 1]
            for c in range(capacity + 1):
                dp[i][c] = dp[i - 1][c]
                if c >= w:
                    dp[i][c] = max(dp[i][c], dp[i - 1][c - w] + v)
        return dp[n][capacity]

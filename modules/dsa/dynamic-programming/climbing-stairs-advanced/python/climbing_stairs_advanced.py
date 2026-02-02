from typing import List

class Solution:
    def climbStairsAdvanced(self, n: int, steps: List[int]) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            total = 0
            for step in steps:
                if i >= step:
                    total += dp[i - step]
            dp[i] = total
        return dp[n]

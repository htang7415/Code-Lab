class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            total = 0
            for root in range(1, i + 1):
                total += dp[root - 1] * dp[i - root]
            dp[i] = total
        return dp[n]

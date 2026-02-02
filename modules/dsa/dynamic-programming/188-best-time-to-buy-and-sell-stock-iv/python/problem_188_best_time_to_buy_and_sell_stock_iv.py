from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0
        n = len(prices)
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit
        buy = [float("-inf")] * k
        sell = [0] * k
        for price in prices:
            prev_buy = buy[:]
            prev_sell = sell[:]
            for i in range(k):
                buy[i] = max(prev_buy[i], (prev_sell[i - 1] if i > 0 else 0) - price)
                sell[i] = max(prev_sell[i], buy[i] + price)
        return sell[-1]

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0
        prev1 = 0
        for value in nums:
            current = max(prev1, prev2 + value)
            prev2, prev1 = prev1, current
        return prev1

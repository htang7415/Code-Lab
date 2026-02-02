from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_line(values: List[int]) -> int:
            prev2 = 0
            prev1 = 0
            for value in values:
                current = max(prev1, prev2 + value)
                prev2, prev1 = prev1, current
            return prev1

        return max(rob_line(nums[:-1]), rob_line(nums[1:]))

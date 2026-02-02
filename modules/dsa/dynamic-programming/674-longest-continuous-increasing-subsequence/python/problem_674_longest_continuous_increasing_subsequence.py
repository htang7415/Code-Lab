from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        best = current = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current += 1
            else:
                current = 1
            best = max(best, current)
        return best

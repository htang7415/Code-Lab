from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        prev_diff = 0
        count = 1
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if (diff > 0 and prev_diff <= 0) or (diff < 0 and prev_diff >= 0):
                count += 1
                prev_diff = diff
        return count

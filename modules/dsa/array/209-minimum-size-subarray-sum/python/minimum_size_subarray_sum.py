from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        length = float('inf')
        window_sum = 0

        for right, value in enumerate(nums):
            window_sum += value
            while window_sum >= target:
                length = min(length, right - left + 1)
                window_sum -= nums[left]
                left += 1
        return length if length != float('inf') else 0

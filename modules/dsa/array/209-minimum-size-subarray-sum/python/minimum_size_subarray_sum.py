from typing import List

# (Version 1) Sliding window
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        length = float('inf')
        sum = 0
        while right < len(nums):
            sum += nums[right]
            while sum >= target:
                length = min(length, right - left + 1)
                sum -= nums[left]
                left += 1
            right += 1
        return length if length != float('inf') else 0

# (Version 2) Brute force
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float('inf')
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum >= target:
                    length = min(length, j - i + 1)
                    break
        return length if length != float('inf') else 0

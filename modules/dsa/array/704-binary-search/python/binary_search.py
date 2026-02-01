from typing import List

# (Version 1) Closed Interval, [left, right]
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1 # Define the target in the left-closed right-closed interval, [left, right]
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return -1
# (Version 2) Left-closed right-open interval, [left, right)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) # Define the target in the left-closed right-open interval, [left, right)
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return -1

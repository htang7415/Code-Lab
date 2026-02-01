from typing import List

# (Version 1) Two pointers
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # array is sorted, in increasing order
        n = len(nums)
        # define a new array to store result
        result = [0] * n
        # left pointer
        i = 0
        # right pointer
        j = n - 1
        # result array pointer
        k = n - 1
        while i <= j:
            if nums[i] ** 2 < nums[j] ** 2:
                result[k] = nums[j] ** 2
                j -= 1
            else:
                result[k] = nums[i] ** 2
                i += 1
            k -= 1
        return result
# (Version 2) Sort after square
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] **= 2
        nums.sort()
        return nums

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1

        for write in range(n - 1, -1, -1):
            if nums[left] ** 2 < nums[right] ** 2:
                result[write] = nums[right] ** 2
                right -= 1
            else:
                result[write] = nums[left] ** 2
                left += 1
        return result

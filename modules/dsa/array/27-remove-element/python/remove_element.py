from typing import List

# (Version 1) Fast-slow pointer
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # slow pointer
        slowIndex = 0
        # fast pointer
        for fastIndex in range(len(nums)):
            if val != nums[fastIndex]:
                nums[slowIndex] = nums[fastIndex]
                slowIndex += 1
        return slowIndex
# (Version 2) Brute force
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        size = len(nums)
        while i < size:
            if nums[i] == val:
                for j in range(i + 1, size):
                    nums[j - 1] = nums[j]
                size -= 1
                i -= 1
            i += 1
        return size
# (Version 3) Two pointers, remove elements from both ends
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # left pointer
        left = 0
        # right pointer
        right = len(nums) - 1
        while left <= right:
            # find left pointer position where element equals val
            while left <= right and nums[left] != val:
                left += 1
            # find right pointer position where element not equals val
            while left <= right and nums[right] == val:
                right -= 1
            # overwrite left pointer position with right pointer's element
            if left < right:
                nums[left] = nums[right]
                left += 1
                right -= 1
        return left

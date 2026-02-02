from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k <= 0:
            return []
        deq: deque[int] = deque()
        result: list[int] = []
        for i, num in enumerate(nums):
            while deq and deq[0] <= i - k:
                deq.popleft()
            while deq and nums[deq[-1]] <= num:
                deq.pop()
            deq.append(i)
            if i >= k - 1:
                result.append(nums[deq[0]])
        return result

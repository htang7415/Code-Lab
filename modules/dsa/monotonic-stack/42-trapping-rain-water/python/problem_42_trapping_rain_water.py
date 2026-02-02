from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack: List[int] = []
        trapped = 0
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                bottom = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                width = i - left - 1
                bounded_height = min(h, height[left]) - height[bottom]
                if bounded_height > 0:
                    trapped += width * bounded_height
            stack.append(i)
        return trapped

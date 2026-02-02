from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack: List[int] = []
        max_area = 0
        for i, h in enumerate(heights + [0]):
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                area = height * width
                if area > max_area:
                    max_area = area
            stack.append(i)
        return max_area

from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[0] * n for _ in range(n)]
        startx, starty = 0, 0  # Starting point
        loop, mid = n // 2, n // 2  # Number of loops and middle position
        count = 1  # Counter

        for offset in range(1, loop + 1):
            for i in range(starty, n - offset):
                nums[startx][i] = count
                count += 1
            for i in range(startx, n - offset):
                nums[i][n - offset] = count
                count += 1
            for i in range(n - offset, starty, -1):
                nums[n - offset][i] = count
                count += 1
            for i in range(n - offset, startx, -1):
                nums[i][starty] = count
                count += 1
            startx += 1
            starty += 1
        if n % 2 != 0:
            nums[mid][mid] = count
        return nums
# Version 2
class Solution(object):
    def generateMatrix(self, n):
        nums = [[0] * n for _ in range(n)]
        # Define boundaries
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        num = 1

        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                nums[top][i] = num
                num += 1
            for i in range(top + 1, bottom + 1):
                nums[i][right] = num
                num += 1
            if left < right and top < bottom:
                for i in range(right - 1, left, -1):
                    nums[bottom][i] = num
                    num += 1
                for i in range(bottom, top, -1):
                    nums[i][left] = num
                    num += 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return nums

from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        start_row = 0
        start_col = 0
        layers = n // 2
        mid = n // 2
        value = 1

        for offset in range(1, layers + 1):
            for col in range(start_col, n - offset):
                matrix[start_row][col] = value
                value += 1
            for row in range(start_row, n - offset):
                matrix[row][n - offset] = value
                value += 1
            for col in range(n - offset, start_col, -1):
                matrix[n - offset][col] = value
                value += 1
            for row in range(n - offset, start_row, -1):
                matrix[row][start_col] = value
                value += 1
            start_row += 1
            start_col += 1

        if n % 2 != 0:
            matrix[mid][mid] = value
        return matrix

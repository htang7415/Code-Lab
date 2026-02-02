from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result: list[list[int]] = []
        path: list[int] = []

        def backtrack(start: int) -> None:
            if len(path) == k:
                result.append(path.copy())
                return
            max_start = n - (k - len(path)) + 1
            for i in range(start, max_start + 1):
                path.append(i)
                backtrack(i + 1)
                path.pop()

        backtrack(1)
        return result

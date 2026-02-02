from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result: list[list[int]] = []
        path: list[int] = []
        used = [False] * len(nums)

        def backtrack() -> None:
            if len(path) == len(nums):
                result.append(path.copy())
                return
            for i, value in enumerate(nums):
                if used[i]:
                    continue
                used[i] = True
                path.append(value)
                backtrack()
                path.pop()
                used[i] = False

        backtrack()
        return result

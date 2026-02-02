from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result: list[list[int]] = []
        path: list[int] = []

        def backtrack(start: int) -> None:
            result.append(path.copy())
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return result

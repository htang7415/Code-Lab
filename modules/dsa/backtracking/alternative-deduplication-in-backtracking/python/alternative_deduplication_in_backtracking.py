from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result: list[list[int]] = []
        path: list[int] = []

        def backtrack(start: int) -> None:
            result.append(path.copy())
            used: set[int] = set()
            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue
                used.add(nums[i])
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return result

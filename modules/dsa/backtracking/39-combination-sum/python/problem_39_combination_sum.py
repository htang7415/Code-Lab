from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result: list[list[int]] = []
        path: list[int] = []

        def backtrack(start: int, remaining: int) -> None:
            if remaining == 0:
                result.append(path.copy())
                return
            for i in range(start, len(candidates)):
                value = candidates[i]
                if value > remaining:
                    break
                path.append(value)
                backtrack(i, remaining - value)
                path.pop()

        backtrack(0, target)
        return result

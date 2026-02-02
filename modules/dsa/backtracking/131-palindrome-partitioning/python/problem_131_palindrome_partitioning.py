class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result: list[list[str]] = []
        path: list[str] = []

        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start: int) -> None:
            if start == len(s):
                result.append(path.copy())
                return
            for end in range(start, len(s)):
                if is_palindrome(start, end):
                    path.append(s[start : end + 1])
                    backtrack(end + 1)
                    path.pop()

        backtrack(0)
        return result

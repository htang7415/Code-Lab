class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        result: list[str] = []
        path: list[str] = []

        def is_valid(segment: str) -> bool:
            if not segment:
                return False
            if len(segment) > 1 and segment[0] == "0":
                return False
            return 0 <= int(segment) <= 255

        def backtrack(start: int) -> None:
            if len(path) == 4:
                if start == len(s):
                    result.append(".".join(path))
                return
            for end in range(start + 1, min(start + 4, len(s) + 1)):
                segment = s[start:end]
                if is_valid(segment):
                    path.append(segment)
                    backtrack(end)
                    path.pop()

        backtrack(0)
        return result

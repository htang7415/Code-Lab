class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s:
            return False
        doubled = s + s
        return s in doubled[1:-1]

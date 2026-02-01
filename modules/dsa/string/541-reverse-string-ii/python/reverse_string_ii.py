class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chars = list(s)
        step = 2 * k
        for start in range(0, len(chars), step):
            i = start
            j = min(start + k - 1, len(chars) - 1)
            while i < j:
                chars[i], chars[j] = chars[j], chars[i]
                i += 1
                j -= 1
        return "".join(chars)

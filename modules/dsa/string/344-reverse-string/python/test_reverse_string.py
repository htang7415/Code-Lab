from reverse_string import Solution

def test_reverse_string_basic():
    chars = ["h", "e", "l", "l", "o"]
    Solution().reverseString(chars)
    assert chars == ["o", "l", "l", "e", "h"]

def test_reverse_string_single():
    chars = ["a"]
    Solution().reverseString(chars)
    assert chars == ["a"]

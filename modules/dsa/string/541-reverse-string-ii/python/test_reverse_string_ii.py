from reverse_string_ii import Solution

def test_reverse_string_ii_example():
    assert Solution().reverseStr("abcdefg", 2) == "bacdfeg"

def test_reverse_string_ii_full():
    assert Solution().reverseStr("abcd", 4) == "dcba"

from implement_strstr import Solution

def test_strstr_found():
    assert Solution().strStr("hello", "ll") == 2

def test_strstr_not_found():
    assert Solution().strStr("aaaaa", "bba") == -1

def test_strstr_empty():
    assert Solution().strStr("", "") == 0

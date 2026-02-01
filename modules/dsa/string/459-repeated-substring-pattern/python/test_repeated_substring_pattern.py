from repeated_substring_pattern import Solution

def test_repeat_true():
    assert Solution().repeatedSubstringPattern("abab") is True

def test_repeat_false():
    assert Solution().repeatedSubstringPattern("aba") is False

def test_repeat_longer():
    assert Solution().repeatedSubstringPattern("abcabcabc") is True

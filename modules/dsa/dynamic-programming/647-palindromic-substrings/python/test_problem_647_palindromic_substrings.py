from problem_647_palindromic_substrings import Solution


def test_palindromic_substrings_basic():
    assert Solution().countSubstrings("abc") == 3


def test_palindromic_substrings_more():
    assert Solution().countSubstrings("aaa") == 6

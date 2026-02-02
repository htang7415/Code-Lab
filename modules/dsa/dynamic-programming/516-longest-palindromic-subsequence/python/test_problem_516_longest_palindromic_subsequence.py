from problem_516_longest_palindromic_subsequence import Solution


def test_lps_basic():
    assert Solution().longestPalindromeSubseq("bbbab") == 4


def test_lps_small():
    assert Solution().longestPalindromeSubseq("cbbd") == 2

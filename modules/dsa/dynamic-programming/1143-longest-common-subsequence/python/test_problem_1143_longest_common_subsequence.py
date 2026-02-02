from problem_1143_longest_common_subsequence import Solution


def test_lcs_basic():
    assert Solution().longestCommonSubsequence("abcde", "ace") == 3


def test_lcs_same():
    assert Solution().longestCommonSubsequence("abc", "abc") == 3

from problem_1143_longest_common_subsequence import Solution


def test_lcs_example():
    assert Solution().longestCommonSubsequence("abcde", "ace") == 3


def test_lcs_edge_empty():
    assert Solution().longestCommonSubsequence("", "abc") == 0


def test_lcs_tricky_repeated_structure():
    assert Solution().longestCommonSubsequence("abcba", "abcbcba") == 5

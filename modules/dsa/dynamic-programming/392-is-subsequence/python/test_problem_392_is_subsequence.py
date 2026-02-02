from problem_392_is_subsequence import Solution


def test_is_subsequence_true():
    assert Solution().isSubsequence("abc", "ahbgdc") is True


def test_is_subsequence_false():
    assert Solution().isSubsequence("axc", "ahbgdc") is False

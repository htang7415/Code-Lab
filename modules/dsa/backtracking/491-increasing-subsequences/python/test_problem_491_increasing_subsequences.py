from problem_491_increasing_subsequences import Solution


def test_increasing_subsequences_basic():
    result = Solution().findSubsequences([4, 6, 7, 7])
    assert [4, 6] in result
    assert [4, 7] in result
    assert [6, 7, 7] in result

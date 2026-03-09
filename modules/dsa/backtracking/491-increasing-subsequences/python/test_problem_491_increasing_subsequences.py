from problem_491_increasing_subsequences import Solution


def test_increasing_subsequences_example():
    result = Solution().findSubsequences([4, 6, 7, 7])
    assert [4, 6] in result
    assert [4, 7] in result
    assert [6, 7, 7] in result


def test_increasing_subsequences_edge_decreasing():
    assert Solution().findSubsequences([4, 3, 2, 1]) == []


def test_increasing_subsequences_tricky_duplicates():
    result = Solution().findSubsequences([1, 1, 1])
    assert sorted(result) == [[1, 1], [1, 1, 1]]

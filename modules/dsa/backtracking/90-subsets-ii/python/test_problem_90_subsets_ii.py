from problem_90_subsets_ii import Solution


def test_subsets_with_dup_basic():
    result = Solution().subsetsWithDup([1, 2, 2])
    assert sorted(result) == [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

from problem_78_subsets import Solution


def test_subsets_basic():
    result = Solution().subsets([1, 2])
    assert sorted(result) == [[], [1], [1, 2], [2]]

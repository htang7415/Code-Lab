from problem_47_permutations_ii import Solution


def test_permutations_unique_basic():
    result = Solution().permuteUnique([1, 1, 2])
    assert sorted(result) == [[1, 1, 2], [1, 2, 1], [2, 1, 1]]

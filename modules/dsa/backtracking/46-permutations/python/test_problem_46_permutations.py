from problem_46_permutations import Solution


def test_permutations_basic():
    result = Solution().permute([1, 2, 3])
    assert len(result) == 6
    assert [1, 2, 3] in result
    assert [3, 2, 1] in result

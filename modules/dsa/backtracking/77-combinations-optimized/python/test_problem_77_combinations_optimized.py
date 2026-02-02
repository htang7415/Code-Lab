from problem_77_combinations_optimized import Solution


def test_combinations_optimized_basic():
    result = Solution().combine(4, 2)
    assert sorted(result) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

from problem_18_4sum import Solution


def test_four_sum_example():
    result = Solution().fourSum([1, 0, -1, 0, -2, 2], 0)
    normalized = sorted(sorted(quad) for quad in result)
    assert normalized == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]


def test_four_sum_edge_none():
    assert Solution().fourSum([2, 2, 2, 2], 9) == []


def test_four_sum_tricky_duplicates():
    assert Solution().fourSum([2, 2, 2, 2, 2], 8) == [[2, 2, 2, 2]]

from problem_15_3sum import Solution


def test_three_sum_basic():
    result = Solution().threeSum([-1, 0, 1, 2, -1, -4])
    normalized = sorted(sorted(triplet) for triplet in result)
    assert normalized == [[-1, -1, 2], [-1, 0, 1]]


def test_three_sum_none():
    assert Solution().threeSum([0, 1, 1]) == []

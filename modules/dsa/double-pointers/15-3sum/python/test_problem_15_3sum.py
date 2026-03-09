from problem_15_3sum import Solution


def test_three_sum_example():
    result = Solution().threeSum([-1, 0, 1, 2, -1, -4])
    normalized = sorted(sorted(triplet) for triplet in result)
    assert normalized == [[-1, -1, 2], [-1, 0, 1]]


def test_three_sum_edge_none():
    assert Solution().threeSum([0, 1, 1]) == []


def test_three_sum_tricky_all_zeroes():
    assert Solution().threeSum([0, 0, 0, 0]) == [[0, 0, 0]]

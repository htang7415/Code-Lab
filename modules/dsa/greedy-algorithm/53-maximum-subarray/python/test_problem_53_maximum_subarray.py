from problem_53_maximum_subarray import Solution


def test_max_subarray_basic():
    assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_max_subarray_single():
    assert Solution().maxSubArray([1]) == 1

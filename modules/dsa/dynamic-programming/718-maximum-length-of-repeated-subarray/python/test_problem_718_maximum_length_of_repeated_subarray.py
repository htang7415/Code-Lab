from problem_718_maximum_length_of_repeated_subarray import Solution


def test_repeated_subarray_basic():
    assert Solution().findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]) == 3


def test_repeated_subarray_all_equal():
    assert Solution().findLength([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]) == 5

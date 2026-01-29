from prefix_sum import build_prefix_sum, range_sum


def test_build_prefix_sum():
    assert build_prefix_sum([]) == [0]
    assert build_prefix_sum([5]) == [0, 5]
    assert build_prefix_sum([1, 2, 3, 4]) == [0, 1, 3, 6, 10]


def test_range_sum_full():
    prefix = build_prefix_sum([1, 2, 3, 4, 5])
    assert range_sum(prefix, 0, 4) == 15


def test_range_sum_subarray():
    prefix = build_prefix_sum([1, 2, 3, 4, 5])
    assert range_sum(prefix, 1, 3) == 9  # 2+3+4


def test_range_sum_single():
    prefix = build_prefix_sum([10, 20, 30])
    assert range_sum(prefix, 1, 1) == 20

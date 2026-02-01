from problem_454_4sum_ii import four_sum_count


def test_four_sum_count_example():
    assert four_sum_count([1, 2], [-2, -1], [-1, 2], [0, 2]) == 2


def test_four_sum_count_zero():
    assert four_sum_count([0], [0], [0], [0]) == 1

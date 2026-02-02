from problem_452_minimum_number_of_arrows_to_burst_balloons import Solution


def test_min_arrows_basic():
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    assert Solution().findMinArrowShots(points) == 2


def test_min_arrows_single():
    points = [[1, 2]]
    assert Solution().findMinArrowShots(points) == 1

from problem_72_edit_distance import Solution


def test_edit_distance_basic():
    assert Solution().minDistance("horse", "ros") == 3


def test_edit_distance_more():
    assert Solution().minDistance("intention", "execution") == 5

from problem_239_sliding_window_maximum import Solution


def test_sliding_window_basic():
    assert Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]


def test_sliding_window_single():
    assert Solution().maxSlidingWindow([1], 1) == [1]

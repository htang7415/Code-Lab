from problem_435_non_overlapping_intervals import Solution


def test_non_overlapping_basic():
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    assert Solution().eraseOverlapIntervals(intervals) == 1


def test_non_overlapping_more():
    intervals = [[1, 2], [1, 2], [1, 2]]
    assert Solution().eraseOverlapIntervals(intervals) == 2

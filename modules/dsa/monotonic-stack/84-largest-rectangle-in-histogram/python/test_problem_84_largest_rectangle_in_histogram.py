from problem_84_largest_rectangle_in_histogram import Solution


def test_largest_rectangle_example():
    heights = [2, 1, 5, 6, 2, 3]
    assert Solution().largestRectangleArea(heights) == 10


def test_largest_rectangle_two_bars():
    heights = [2, 4]
    assert Solution().largestRectangleArea(heights) == 4

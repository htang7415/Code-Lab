from problem_84_largest_rectangle_in_histogram import Solution


def test_largest_rectangle_example():
    heights = [2, 1, 5, 6, 2, 3]
    assert Solution().largestRectangleArea(heights) == 10


def test_largest_rectangle_edge_single_bar():
    heights = [2]
    assert Solution().largestRectangleArea(heights) == 2


def test_largest_rectangle_tricky_increasing():
    heights = [1, 2, 3, 4, 5]
    assert Solution().largestRectangleArea(heights) == 9

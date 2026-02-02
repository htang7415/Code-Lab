from problem_279_perfect_squares import Solution


def test_perfect_squares_basic():
    assert Solution().numSquares(12) == 3


def test_perfect_squares_more():
    assert Solution().numSquares(13) == 2

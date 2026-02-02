from problem_51_n_queens import Solution


def test_n_queens_4():
    result = Solution().solveNQueens(4)
    assert len(result) == 2

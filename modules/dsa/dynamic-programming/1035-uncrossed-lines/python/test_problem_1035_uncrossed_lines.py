from problem_1035_uncrossed_lines import Solution


def test_uncrossed_lines_example():
    assert Solution().maxUncrossedLines([1, 4, 2], [1, 2, 4]) == 2


def test_uncrossed_lines_edge_empty():
    assert Solution().maxUncrossedLines([], [1, 2, 3]) == 0


def test_uncrossed_lines_tricky_duplicates():
    assert Solution().maxUncrossedLines([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]) == 2

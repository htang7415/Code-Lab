from problem_45_jump_game_ii import Solution


def test_jump_game_ii_basic():
    assert Solution().jump([2, 3, 1, 1, 4]) == 2


def test_jump_game_ii_single():
    assert Solution().jump([0]) == 0

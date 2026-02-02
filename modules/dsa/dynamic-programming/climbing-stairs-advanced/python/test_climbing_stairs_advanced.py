from climbing_stairs_advanced import Solution


def test_climb_stairs_advanced_basic():
    assert Solution().climbStairsAdvanced(4, [1, 2]) == 5


def test_climb_stairs_advanced_more():
    assert Solution().climbStairsAdvanced(4, [1, 3, 5]) == 3

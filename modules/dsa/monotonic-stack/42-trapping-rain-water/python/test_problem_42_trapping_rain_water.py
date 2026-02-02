from problem_42_trapping_rain_water import Solution


def test_trap_rain_water_classic():
    heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    assert Solution().trap(heights) == 6


def test_trap_rain_water_valleys():
    heights = [4, 2, 0, 3, 2, 5]
    assert Solution().trap(heights) == 9

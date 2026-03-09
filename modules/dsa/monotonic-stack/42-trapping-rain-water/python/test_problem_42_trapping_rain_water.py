from problem_42_trapping_rain_water import Solution


def test_trap_rain_water_example():
    heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    assert Solution().trap(heights) == 6


def test_trap_rain_water_edge_monotonic():
    heights = [1, 2, 3, 4]
    assert Solution().trap(heights) == 0


def test_trap_rain_water_tricky_valleys():
    heights = [4, 2, 0, 3, 2, 5]
    assert Solution().trap(heights) == 9

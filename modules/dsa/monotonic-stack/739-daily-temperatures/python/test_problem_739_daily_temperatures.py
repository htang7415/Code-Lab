from problem_739_daily_temperatures import Solution


def test_daily_temperatures_mixed():
    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    assert Solution().dailyTemperatures(temps) == [1, 1, 4, 2, 1, 1, 0, 0]


def test_daily_temperatures_increasing():
    temps = [30, 40, 50, 60]
    assert Solution().dailyTemperatures(temps) == [1, 1, 1, 0]

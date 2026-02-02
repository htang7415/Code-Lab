from problem_134_gas_station import Solution


def test_gas_station_basic():
    assert Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3


def test_gas_station_impossible():
    assert Solution().canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1

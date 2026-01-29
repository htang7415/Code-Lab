from solution import two_sum


def test_example_1():
    assert sorted(two_sum([2, 7, 11, 15], 9)) == [0, 1]


def test_example_2():
    assert sorted(two_sum([3, 2, 4], 6)) == [1, 2]


def test_duplicates():
    assert sorted(two_sum([3, 3], 6)) == [0, 1]


def test_negative_numbers():
    assert sorted(two_sum([-1, -2, -3, -4, -5], -8)) == [2, 4]


def test_large_target():
    assert sorted(two_sum([1000000000, 2, 1000000000], 2000000000)) == [0, 2]

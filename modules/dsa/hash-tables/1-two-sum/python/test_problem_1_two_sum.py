from problem_1_two_sum import two_sum


def test_two_sum_basic():
    assert sorted(two_sum([2, 7, 11, 15], 9)) == [0, 1]


def test_two_sum_duplicates():
    assert sorted(two_sum([3, 3], 6)) == [0, 1]

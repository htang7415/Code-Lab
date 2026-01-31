from accuracy import accuracy


def test_accuracy():
    assert accuracy([1, 0, 1], [1, 1, 1]) == 2 / 3

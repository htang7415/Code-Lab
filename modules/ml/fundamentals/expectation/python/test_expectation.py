from expectation import expectation


def test_expectation():
    assert expectation([0, 1], [0.5, 0.5]) == 0.5

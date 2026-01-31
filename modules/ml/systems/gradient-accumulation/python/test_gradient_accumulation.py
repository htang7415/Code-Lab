from gradient_accumulation import accumulate


def test_accumulate():
    assert accumulate([[1.0, 2.0], [3.0, 4.0]]) == [4.0, 6.0]

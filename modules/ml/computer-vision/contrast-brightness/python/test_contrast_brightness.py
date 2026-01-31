from contrast_brightness import adjust


def test_adjust():
    assert adjust(10.0, 1.0, 5.0) == 15.0

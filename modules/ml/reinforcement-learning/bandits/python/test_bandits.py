from bandits import update_value


def test_update_value():
    assert update_value(0.0, 1, 1.0) == 1.0

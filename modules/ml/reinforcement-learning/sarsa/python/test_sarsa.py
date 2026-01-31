from sarsa import sarsa_update


def test_sarsa_update():
    assert sarsa_update(0.0, 1.0, 0.0, 0.5, 0.9) == 0.5

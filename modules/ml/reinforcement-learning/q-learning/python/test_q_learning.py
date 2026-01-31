from q_learning import q_update


def test_q_update():
    assert q_update(0.0, 1.0, 0.0, 0.5, 0.9) == 0.5

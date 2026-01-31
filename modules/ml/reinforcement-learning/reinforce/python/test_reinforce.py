from reinforce import reinforce_update


def test_reinforce_update():
    assert reinforce_update(2.0, 1.0, 0.1) == 0.2

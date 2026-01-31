from adamw import adamw_step


def test_adamw_step():
    w, m, v = adamw_step(1.0, 1.0, 0.0, 0.0, 0.1, 0.1, 0.9, 0.999, 1e-8)
    assert w < 1.0

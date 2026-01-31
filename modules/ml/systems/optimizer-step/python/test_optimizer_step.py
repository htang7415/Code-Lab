from optimizer_step import step


def test_step():
    assert step(1.0, 0.5, 0.1) == 0.95

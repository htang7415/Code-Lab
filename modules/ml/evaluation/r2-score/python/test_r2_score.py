from r2_score import r2_score


def test_r2_score():
    assert r2_score([1.0, 2.0], [1.0, 2.0]) == 1.0

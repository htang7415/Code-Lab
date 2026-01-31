from l2_regularization import l2_penalty


def test_l2_penalty():
    assert l2_penalty([1.0, -2.0], 0.1) == 0.5

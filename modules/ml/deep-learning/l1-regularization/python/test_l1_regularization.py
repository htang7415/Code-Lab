from l1_regularization import l1_penalty


def test_l1_penalty():
    assert l1_penalty([1.0, -2.0], 0.1) == 0.3

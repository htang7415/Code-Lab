from kl_regularization import kl_penalty


def test_kl_penalty():
    p = [0.5, 0.5]
    q = [0.9, 0.1]
    penalty = kl_penalty(p, q, beta=0.1)
    assert penalty > 0.0

from distributions import normalize_probs


def test_normalize_probs():
    probs = normalize_probs([1.0, 1.0])
    assert abs(sum(probs) - 1.0) < 1e-6

from adaboost import update_weights


def test_update_weights():
    out = update_weights([0.5, 0.5], [1, 0], 0.7)
    assert abs(sum(out) - 1.0) < 1e-6

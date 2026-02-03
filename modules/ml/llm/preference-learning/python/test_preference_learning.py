import math

from preference_learning import preference_loss


def test_preference_loss():
    loss = preference_loss(2.0, 0.5)
    expected = math.log1p(math.exp(-(2.0 - 0.5)))
    assert math.isclose(loss, expected, rel_tol=1e-6)

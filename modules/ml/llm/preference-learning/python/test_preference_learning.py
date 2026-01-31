from preference_learning import preference_loss


def test_preference_loss():
    loss = preference_loss(2.0, 0.5)
    assert loss < 0.2

from focal_loss import focal_loss


def test_focal_loss():
    assert focal_loss(0.9, gamma=2.0) < focal_loss(0.6, gamma=2.0)

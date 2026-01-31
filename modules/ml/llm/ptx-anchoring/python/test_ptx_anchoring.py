from ptx_anchoring import anchored_loss


def test_anchored_loss():
    loss = anchored_loss(1.0, 0.5, 0.2)
    assert abs(loss - 0.9) < 1e-6

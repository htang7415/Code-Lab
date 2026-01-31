from hinge_loss import hinge_loss


def test_hinge_loss():
    assert hinge_loss(2.0, 1) == 0.0
    assert hinge_loss(0.2, 1) == 0.8

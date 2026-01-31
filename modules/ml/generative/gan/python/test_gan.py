from gan import gan_loss


def test_gan_loss():
    assert gan_loss(0.9, 0.1) < gan_loss(0.6, 0.4)

from loss_scaling import scale_grad


def test_scale_grad():
    assert scale_grad(0.5, 8.0) == 4.0

from lr_constant import constant_lr


def test_constant_lr():
    assert constant_lr(0.1) == 0.1

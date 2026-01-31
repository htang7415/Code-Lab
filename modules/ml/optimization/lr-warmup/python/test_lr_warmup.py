from lr_warmup import warmup_lr


def test_warmup_lr():
    assert warmup_lr(1.0, 5, 10) == 0.5

from huber_loss import huber


def test_huber():
    assert huber(1.0, 0.0, delta=1.0) == 0.5

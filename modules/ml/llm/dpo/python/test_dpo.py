from dpo import dpo_loss


def test_dpo_loss():
    loss = dpo_loss(1.0, 0.2, beta=0.5)
    assert loss < 0.6

from knowledge_distillation_loss import distill_loss


def test_distill_loss():
    loss = distill_loss([2.0, 0.0], [2.0, 0.0], temp=1.0)
    assert loss < 1e-6

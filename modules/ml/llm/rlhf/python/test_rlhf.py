from rlhf import reward_model_loss


def test_reward_model_loss():
    loss = reward_model_loss(1.2, 0.0)
    assert loss < 0.4

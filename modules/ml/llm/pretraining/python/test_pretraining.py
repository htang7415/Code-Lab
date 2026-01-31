from pretraining import next_token_loss


def test_next_token_loss():
    logits = [[2.0, 0.0], [0.0, 2.0]]
    loss = next_token_loss(logits, [0, 1])
    assert loss < 0.2

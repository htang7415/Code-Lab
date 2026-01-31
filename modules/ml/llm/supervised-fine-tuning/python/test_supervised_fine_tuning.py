from supervised_fine_tuning import sft_loss


def test_sft_loss_mask():
    logits = [[2.0, 0.0], [0.0, 2.0]]
    loss = sft_loss(logits, [0, 1], [1, 0])
    assert loss < 0.2

from contrastive_loss import info_nce_loss


def test_info_nce_prefers_positive():
    anchor = [1.0, 0.0]
    positive = [1.0, 0.0]
    negatives = [[0.0, 1.0]]
    loss_good = info_nce_loss(anchor, positive, negatives, temperature=0.5)

    positive_bad = [0.0, 1.0]
    negatives_bad = [[1.0, 0.0]]
    loss_bad = info_nce_loss(anchor, positive_bad, negatives_bad, temperature=0.5)

    assert loss_good < loss_bad

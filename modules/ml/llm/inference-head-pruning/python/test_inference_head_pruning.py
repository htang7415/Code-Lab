from inference_head_pruning import prune_heads


def test_prune_heads():
    weights = [[1.0, 2.0, 3.0, 4.0]]
    pruned = prune_heads(weights, keep=[1], head_dim=2)
    assert pruned == [[3.0, 4.0]]

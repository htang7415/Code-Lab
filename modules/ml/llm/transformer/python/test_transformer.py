from transformer import transformer_block


def test_transformer_block_shape():
    x = [[0.1, 0.2], [0.0, 0.3]]
    w1 = [[0.5, 0.0], [0.0, 0.5]]
    w2 = [[1.0, 0.0], [0.0, 1.0]]
    out = transformer_block(x, w1, w2)
    assert len(out) == 2
    assert len(out[0]) == 2

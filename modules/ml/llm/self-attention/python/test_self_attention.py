from self_attention import self_attention


def test_self_attention_shape():
    q = [[1.0, 0.0], [0.0, 1.0]]
    k = [[1.0, 0.0], [0.0, 1.0]]
    v = [[1.0, 2.0], [3.0, 4.0]]
    out = self_attention(q, k, v)
    assert len(out) == 2
    assert len(out[0]) == 2

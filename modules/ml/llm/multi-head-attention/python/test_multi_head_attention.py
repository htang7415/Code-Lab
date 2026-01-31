from multi_head_attention import multi_head_attention


def test_multi_head_attention_shape():
    q = [[1.0, 0.0, 0.0, 1.0]] * 2
    out = multi_head_attention(q, q, q, heads=2)
    assert len(out) == 2
    assert len(out[0]) == 4

from embeddings import embed


def test_embed_lookup():
    table = [[0.0, 0.1], [1.0, 1.1], [2.0, 2.1]]
    out = embed([2, 0], table)
    assert out == [[2.0, 2.1], [0.0, 0.1]]

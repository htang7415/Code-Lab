from qlora import qlora_update


def test_qlora_update():
    w = [[1.05, 0.0], [0.0, 1.0]]
    a = [[1.0], [0.0]]
    b = [[2.0, 0.0]]
    out = qlora_update(w, a, b, alpha=1.0, scale=0.1)
    assert out[0][0] > 1.0

from lora import lora_update


def test_lora_update():
    w = [[1.0, 0.0], [0.0, 1.0]]
    a = [[1.0], [0.0]]
    b = [[2.0, 0.0]]
    out = lora_update(w, a, b, alpha=1.0)
    assert out[0][0] > 1.0

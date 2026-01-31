from int8_int4_quantization import quantize_int


def test_quantize_int():
    q = quantize_int(1.2, bits=4, scale=0.1)
    assert q <= 7

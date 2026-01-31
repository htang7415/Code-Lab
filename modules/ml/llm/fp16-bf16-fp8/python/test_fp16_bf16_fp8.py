from fp16_bf16_fp8 import quantize_fp


def test_quantize_fp():
    out = quantize_fp(1.2345, mantissa_bits=3)
    assert abs(out - 1.25) < 0.1

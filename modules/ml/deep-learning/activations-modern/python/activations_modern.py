import math


def modern_activations(x: float) -> dict[str, float]:
    sigmoid = 1 / (1 + math.exp(-x))
    swish = x * sigmoid
    gelu = 0.5 * x * (1 + math.tanh(math.sqrt(2 / math.pi) * (x + 0.044715 * x**3)))
    mish = x * math.tanh(math.log1p(math.exp(x)))
    swiglu = (x * sigmoid) * x
    return {"swish": swish, "gelu": gelu, "mish": mish, "swiglu": swiglu}

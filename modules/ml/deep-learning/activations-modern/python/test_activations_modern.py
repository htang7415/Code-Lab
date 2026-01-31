from activations_modern import modern_activations


def test_modern_activations():
    out = modern_activations(1.0)
    assert "gelu" in out

from jensen_shannon_divergence import js


def test_js():
    assert js([0.5, 0.5], [0.5, 0.5]) == 0.0

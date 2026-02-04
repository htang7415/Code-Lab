from lenet_5 import layers


def test_layers():
    plan = layers()
    assert plan[0] == "conv5x5"
    assert plan.count("fc") == 3

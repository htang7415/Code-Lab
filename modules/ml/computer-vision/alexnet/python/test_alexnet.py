from alexnet import layers


def test_layers():
    plan = layers()
    assert plan[0] == "conv11x11"
    assert plan.count("dropout") == 2

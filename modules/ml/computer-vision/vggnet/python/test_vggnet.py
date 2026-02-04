from vggnet import layers


def test_layers():
    plan = layers()
    assert plan.count("conv3x3") == 4
    assert plan.count("fc") == 3

from resnet import layers


def test_layers():
    assert layers() == [
        "stem",
        "residual-stage-1",
        "residual-stage-2",
        "residual-stage-3",
        "residual-stage-4",
        "global-average-pool",
        "fully-connected",
    ]

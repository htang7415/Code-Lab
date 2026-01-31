from non_maximum_suppression import iou


def test_iou():
    assert iou((0, 0, 1, 1), (0, 0, 1, 1)) == 1.0

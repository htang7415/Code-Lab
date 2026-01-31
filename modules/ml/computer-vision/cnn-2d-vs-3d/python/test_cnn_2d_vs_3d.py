from cnn_2d_vs_3d import output_depth


def test_output_depth():
    assert output_depth(5, 3) == 3

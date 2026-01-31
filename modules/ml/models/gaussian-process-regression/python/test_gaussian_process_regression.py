from gaussian_process_regression import rbf_kernel


def test_rbf_kernel():
    assert abs(rbf_kernel([0.0], [0.0], 1.0) - 1.0) < 1e-6

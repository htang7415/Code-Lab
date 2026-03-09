import pytest

from kernel_pca import centered_rbf_kernel


def test_centered_rbf_kernel_symmetric_and_centered():
    kernel = centered_rbf_kernel([[0.0], [1.0]], gamma=1.0)
    assert kernel[0][1] == pytest.approx(kernel[1][0])
    assert sum(kernel[0]) == pytest.approx(0.0)
    assert sum(kernel[1]) == pytest.approx(0.0)


def test_centered_rbf_kernel_single_point_is_zero():
    assert centered_rbf_kernel([[2.0, 3.0]], gamma=0.5) == [[0.0]]

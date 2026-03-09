import pytest

from vectors_matrices import matvec


def test_matvec():
    assert matvec([[1.0, 0.0], [0.0, 1.0]], [2.0, 3.0]) == [2.0, 3.0]


def test_matvec_nontrivial_linear_map():
    assert matvec([[2.0, -1.0], [0.5, 3.0]], [4.0, 2.0]) == [6.0, 8.0]


def test_matvec_rejects_dimension_mismatch():
    with pytest.raises(ValueError, match="x length"):
        matvec([[1.0, 2.0]], [1.0])

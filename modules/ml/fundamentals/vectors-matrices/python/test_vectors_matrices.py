from vectors_matrices import matvec


def test_matvec():
    assert matvec([[1.0, 0.0], [0.0, 1.0]], [2.0, 3.0]) == [2.0, 3.0]

from muon_optimizer import gram_schmidt_rows, muon_step


def test_gram_schmidt_rows_orthogonal():
    mat = [[1.0, 2.0], [3.0, 4.0]]
    q = gram_schmidt_rows(mat)
    dot = q[0][0] * q[1][0] + q[0][1] * q[1][1]
    assert abs(dot) < 1e-6


def test_muon_step_updates_weights():
    weights = [[1.0, 0.0], [0.0, 1.0]]
    grad = [[1.0, 0.0], [0.0, 1.0]]
    new_weights, velocity = muon_step(weights, grad, None, lr=0.1, momentum=0.0)
    assert velocity == grad
    assert new_weights[0][0] != weights[0][0]

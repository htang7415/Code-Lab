from feature_drift_psi import psi


def test_psi_zero():
    assert abs(psi([0.5, 0.5], [0.5, 0.5])) < 1e-6

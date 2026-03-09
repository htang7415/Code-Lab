import pytest

from gaussian_mixture_model_em import em_step_1d


def test_em_step_1d_updates_toward_cluster_means():
    weights, means, variances = em_step_1d(
        data=[0.0, 0.2, 10.0, 10.2],
        weights=[0.5, 0.5],
        means=[0.0, 10.0],
        variances=[1.0, 1.0],
    )

    assert weights[0] == pytest.approx(0.5, abs=1e-3)
    assert weights[1] == pytest.approx(0.5, abs=1e-3)
    assert means[0] == pytest.approx(0.1, abs=1e-2)
    assert means[1] == pytest.approx(10.1, abs=1e-2)
    assert variances[0] == pytest.approx(0.01, abs=1e-2)
    assert variances[1] == pytest.approx(0.01, abs=1e-2)

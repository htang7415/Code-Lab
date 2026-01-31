from etl_pipeline import normalize


def test_normalize_mean():
    out = normalize([1.0, 2.0, 3.0])
    assert abs(sum(out)) < 1e-6

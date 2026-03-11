from cardinality_estimation import (
    choose_access_path,
    estimate_rows,
    needs_plan_attention,
    q_error,
)


def test_estimate_rows_multiplies_selectivities() -> None:
    assert estimate_rows(10_000, [0.1, 0.2]) == 200


def test_access_path_prefers_index_for_small_estimated_fraction() -> None:
    estimated_rows = estimate_rows(10_000, [0.01])

    assert choose_access_path(estimated_rows, 10_000, index_available=True) == "index-scan"
    assert choose_access_path(estimated_rows, 10_000, index_available=False) == "seq-scan"


def test_q_error_flags_large_misestimates() -> None:
    estimated_rows = 200
    actual_rows = 1_200

    assert q_error(estimated_rows, actual_rows) == 6.0
    assert needs_plan_attention(estimated_rows, actual_rows) is True

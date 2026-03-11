from window_functions_basics import (
    best_run_per_model,
    create_connection,
    create_eval_results_table,
    rank_runs_within_model,
    record_eval_result,
    score_deltas_by_model,
)


def seed_eval_rows() -> list[tuple[str, str, float, str]]:
    return [
        ("gpt-mini", "helpfulness", 0.81, "2026-03-01T09:00:00Z"),
        ("gpt-mini", "helpfulness", 0.84, "2026-03-02T09:00:00Z"),
        ("rag-large", "grounding", 0.90, "2026-03-01T10:00:00Z"),
        ("rag-large", "grounding", 0.88, "2026-03-02T10:00:00Z"),
    ]


def build_seeded_connection():
    conn = create_connection()
    create_eval_results_table(conn)
    for row in seed_eval_rows():
        record_eval_result(conn, *row)
    return conn


def test_row_number_ranks_rows_inside_each_model_partition() -> None:
    conn = build_seeded_connection()

    assert rank_runs_within_model(conn) == [
        {
            "model_name": "gpt-mini",
            "dataset_name": "helpfulness",
            "score": 0.84,
            "recorded_at": "2026-03-02T09:00:00Z",
            "rank_in_model": 1,
        },
        {
            "model_name": "gpt-mini",
            "dataset_name": "helpfulness",
            "score": 0.81,
            "recorded_at": "2026-03-01T09:00:00Z",
            "rank_in_model": 2,
        },
        {
            "model_name": "rag-large",
            "dataset_name": "grounding",
            "score": 0.9,
            "recorded_at": "2026-03-01T10:00:00Z",
            "rank_in_model": 1,
        },
        {
            "model_name": "rag-large",
            "dataset_name": "grounding",
            "score": 0.88,
            "recorded_at": "2026-03-02T10:00:00Z",
            "rank_in_model": 2,
        },
    ]


def test_best_run_per_model_uses_score_then_newer_timestamp_as_tie_breaker() -> None:
    conn = create_connection()
    create_eval_results_table(conn)
    record_eval_result(conn, "gpt-mini", "helpfulness", 0.84, "2026-03-01T09:00:00Z")
    record_eval_result(conn, "gpt-mini", "helpfulness", 0.84, "2026-03-02T09:00:00Z")
    record_eval_result(conn, "rag-large", "grounding", 0.90, "2026-03-01T10:00:00Z")

    assert best_run_per_model(conn) == [
        {
            "model_name": "gpt-mini",
            "dataset_name": "helpfulness",
            "score": 0.84,
            "recorded_at": "2026-03-02T09:00:00Z",
        },
        {
            "model_name": "rag-large",
            "dataset_name": "grounding",
            "score": 0.9,
            "recorded_at": "2026-03-01T10:00:00Z",
        },
    ]


def test_lag_computes_score_changes_within_each_model() -> None:
    conn = build_seeded_connection()

    assert score_deltas_by_model(conn) == [
        {
            "model_name": "gpt-mini",
            "dataset_name": "helpfulness",
            "score": 0.81,
            "recorded_at": "2026-03-01T09:00:00Z",
            "delta_from_previous": None,
        },
        {
            "model_name": "gpt-mini",
            "dataset_name": "helpfulness",
            "score": 0.84,
            "recorded_at": "2026-03-02T09:00:00Z",
            "delta_from_previous": 0.029999999999999916,
        },
        {
            "model_name": "rag-large",
            "dataset_name": "grounding",
            "score": 0.9,
            "recorded_at": "2026-03-01T10:00:00Z",
            "delta_from_previous": None,
        },
        {
            "model_name": "rag-large",
            "dataset_name": "grounding",
            "score": 0.88,
            "recorded_at": "2026-03-02T10:00:00Z",
            "delta_from_previous": -0.020000000000000018,
        },
    ]

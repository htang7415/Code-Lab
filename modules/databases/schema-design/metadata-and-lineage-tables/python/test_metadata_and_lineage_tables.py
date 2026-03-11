import sqlite3

import pytest

from metadata_and_lineage_tables import (
    create_connection,
    create_metadata_lineage_schema,
    insert_asset,
    insert_job,
    lineage_summary,
    link_job_input,
    link_job_output,
)


def build_seeded_connection():
    conn = create_connection()
    create_metadata_lineage_schema(conn)
    dataset_id = insert_asset(conn, 42, "dataset", "s3://datasets/v1.parquet", "hash-a")
    prompt_id = insert_asset(conn, 42, "prompt", "prompt://summarize/v3", "hash-b")
    output_id = insert_asset(conn, 42, "report", "s3://reports/run-7.json", "hash-c")
    job_id = insert_job(conn, 42, "eval", "gpt-4.1-mini", "2026-03-11T10:00:00Z")
    link_job_input(conn, job_id, dataset_id, "dataset")
    link_job_input(conn, job_id, prompt_id, "prompt")
    link_job_output(conn, job_id, output_id)
    return conn, job_id, output_id


def test_lineage_summary_lists_job_metadata_inputs_and_outputs() -> None:
    conn, job_id, _ = build_seeded_connection()

    assert lineage_summary(conn, job_id) == {
        "job_kind": "eval",
        "model_name": "gpt-4.1-mini",
        "created_at": "2026-03-11T10:00:00Z",
        "inputs": [
            {"role": "dataset", "uri": "s3://datasets/v1.parquet"},
            {"role": "prompt", "uri": "prompt://summarize/v3"},
        ],
        "outputs": [
            {"role": "primary", "uri": "s3://reports/run-7.json"},
        ],
    }


def test_an_asset_can_only_have_one_producer_job() -> None:
    conn, _, output_id = build_seeded_connection()
    other_job_id = insert_job(conn, 42, "eval", "gpt-4.1", "2026-03-11T10:05:00Z")

    with pytest.raises(sqlite3.IntegrityError):
        link_job_output(conn, other_job_id, output_id)


def test_foreign_keys_reject_missing_jobs_or_assets() -> None:
    conn = create_connection()
    create_metadata_lineage_schema(conn)

    with pytest.raises(sqlite3.IntegrityError):
        link_job_input(conn, 999, 888, "dataset")

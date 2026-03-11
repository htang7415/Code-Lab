from multi_tenant_index_design import index_cost_summary, prefix_match_columns


def test_tenant_leading_index_narrows_candidates_for_shared_tables():
    rows = [
        {"id": "d1", "workspace_id": 7, "status": "open", "created_day": 1},
        {"id": "d2", "workspace_id": 8, "status": "open", "created_day": 1},
        {"id": "d3", "workspace_id": 7, "status": "closed", "created_day": 1},
        {"id": "d4", "workspace_id": 8, "status": "closed", "created_day": 1},
        {"id": "d5", "workspace_id": 7, "status": "open", "created_day": 2},
    ]
    filters = {"workspace_id": 7, "status": "open"}

    tenant_first = index_cost_summary(
        rows,
        index_order=("workspace_id", "status", "created_day"),
        filters=filters,
    )
    status_first = index_cost_summary(
        rows,
        index_order=("status", "created_day", "workspace_id"),
        filters=filters,
    )

    assert prefix_match_columns(("workspace_id", "status", "created_day"), filters) == (
        "workspace_id",
        "status",
    )
    assert tenant_first["candidate_count"] == 2
    assert tenant_first["result_ids"] == ["d1", "d5"]
    assert status_first["candidate_count"] == 3
    assert status_first["result_ids"] == ["d1", "d5"]


def test_missing_leading_filter_means_no_prefix_narrowing():
    rows = [
        {"id": "d1", "workspace_id": 7, "status": "open", "created_day": 1},
        {"id": "d2", "workspace_id": 8, "status": "open", "created_day": 1},
    ]

    summary = index_cost_summary(
        rows,
        index_order=("workspace_id", "status"),
        filters={"status": "open"},
    )

    assert summary["matched_prefix"] == []
    assert summary["candidate_count"] == 2
    assert summary["result_count"] == 2

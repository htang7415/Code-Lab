import pytest

from join_order_and_cardinality import cheaper_plan, filtered_rows, left_deep_plan_cost


def test_selective_dimension_first_keeps_intermediate_work_smaller():
    table_rows = {"customers": 100_000, "orders": 500_000, "items": 2_000_000}
    selectivities = {"customers": 0.001, "orders": 1.0, "items": 1.0}
    join_edges = {
        ("customers", "orders"): 5.0,
        ("orders", "items"): 4.0,
        ("items", "orders"): 1.0,
        ("orders", "customers"): 1.0,
    }

    selective_first = left_deep_plan_cost(
        table_rows,
        selectivities,
        ["customers", "orders", "items"],
        join_edges,
    )
    fact_first = left_deep_plan_cost(
        table_rows,
        selectivities,
        ["items", "orders", "customers"],
        join_edges,
    )

    assert selective_first["output_rows"] == 2_000
    assert fact_first["output_rows"] == 2_000_000
    assert cheaper_plan(selective_first, fact_first) == "left"


def test_missing_join_edge_raises():
    with pytest.raises(KeyError):
        left_deep_plan_cost(
            {"a": 10, "b": 20},
            {"a": 1.0, "b": 1.0},
            ["a", "b"],
            {},
        )


def test_filtered_rows_clamps_nonzero_selective_inputs():
    assert filtered_rows(1000, 0.001) == 1
    assert filtered_rows(1000, 0.5) == 500


def test_invalid_selectivity_is_rejected():
    with pytest.raises(ValueError, match="selectivity"):
        filtered_rows(1000, 1.2)

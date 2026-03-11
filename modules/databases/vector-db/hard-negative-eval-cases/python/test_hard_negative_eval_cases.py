from hard_negative_eval_cases import (
    dataset_summary,
    hard_negative_case,
    hard_negative_count,
    invalid_case_ids,
    query_type_counts,
)


def test_dataset_summary_counts_hard_negatives_and_query_types() -> None:
    cases = [
        hard_negative_case("q1", "doc-1", ["doc-2", "doc-3"], "semantic"),
        hard_negative_case("q2", "doc-9", ["doc-8"], "keyword"),
    ]

    assert hard_negative_count(cases) == 3
    assert query_type_counts(cases) == {"keyword": 1, "semantic": 1}
    assert dataset_summary(cases) == {
        "case_count": 2,
        "hard_negative_total": 3,
        "invalid_case_ids": [],
        "query_type_counts": {"keyword": 1, "semantic": 1},
        "ready": True,
    }


def test_invalid_case_ids_flags_empty_and_conflicting_cases() -> None:
    cases = [
        hard_negative_case("q-missing-negs", "doc-1", [], "semantic"),
        hard_negative_case("q-overlap", "doc-7", ["doc-7", "doc-8"], "semantic"),
        hard_negative_case("q-missing-type", "doc-9", ["doc-10"], ""),
    ]

    assert invalid_case_ids(cases) == [
        "q-missing-negs",
        "q-missing-type",
        "q-overlap",
    ]

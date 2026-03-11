from retrieval_evaluation_dataset_shapes import (
    dataset_summary,
    duplicate_query_ids,
    evaluation_case,
    invalid_case_ids,
    query_type_counts,
)


def test_dataset_summary_tracks_query_type_coverage():
    cases = [
        evaluation_case("q1", ["a"], "keyword", 7),
        evaluation_case("q2", ["b"], "semantic", 7),
        evaluation_case("q3", ["c"], "multi-hop", 7),
    ]

    assert query_type_counts(cases) == {"keyword": 1, "semantic": 1, "multi-hop": 1}
    assert dataset_summary(cases)["invalid_case_ids"] == []


def test_dataset_validation_finds_duplicates_and_missing_labels():
    cases = [
        evaluation_case("q1", ["a"], "keyword", 7),
        evaluation_case("q1", ["b"], "semantic", 7),
        evaluation_case("q2", [], "keyword", 7),
    ]

    assert duplicate_query_ids(cases) == ["q1"]
    assert invalid_case_ids(cases) == ["q2"]

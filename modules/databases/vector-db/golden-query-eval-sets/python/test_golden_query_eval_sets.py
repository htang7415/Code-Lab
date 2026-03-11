from golden_query_eval_sets import (
    duplicate_query_ids,
    golden_case,
    golden_set_ready,
    golden_set_summary,
    missing_required_types,
)


def test_ready_golden_set_covers_required_query_types_without_duplicates():
    cases = [
        golden_case("q1", "a", "keyword"),
        golden_case("q2", "b", "semantic"),
        golden_case("q3", "c", "multi-hop"),
    ]

    assert duplicate_query_ids(cases) == []
    assert missing_required_types(cases, ["keyword", "semantic", "multi-hop"]) == []
    assert golden_set_ready(cases, ["keyword", "semantic", "multi-hop"], min_case_count=3) is True


def test_missing_coverage_or_duplicate_ids_make_set_unready():
    cases = [
        golden_case("q1", "a", "keyword"),
        golden_case("q1", "b", "semantic"),
    ]

    assert duplicate_query_ids(cases) == ["q1"]
    assert missing_required_types(cases, ["keyword", "semantic", "multi-hop"]) == ["multi-hop"]
    assert golden_set_summary(cases, ["keyword", "semantic", "multi-hop"], min_case_count=3)["ready"] is False

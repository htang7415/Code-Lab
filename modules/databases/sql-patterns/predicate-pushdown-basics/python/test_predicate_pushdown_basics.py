from predicate_pushdown_basics import (
    group_might_match,
    matching_rows,
    pushdown_summary,
    pushed_down_group_ids,
)


def test_pushdown_skips_groups_whose_stats_cannot_match():
    groups = [
        {"id": "g1", "min_score": 0, "max_score": 40, "rows": []},
        {"id": "g2", "min_score": 50, "max_score": 90, "rows": []},
    ]

    assert not group_might_match(groups[0], min_score=60)
    assert pushed_down_group_ids(groups, min_score=60) == ["g2"]


def test_matching_rows_only_scan_pushed_down_groups():
    groups = [
        {
            "id": "g1",
            "min_score": 0,
            "max_score": 40,
            "rows": [{"id": "a", "score": 10}],
        },
        {
            "id": "g2",
            "min_score": 50,
            "max_score": 90,
            "rows": [{"id": "c", "score": 65}, {"id": "d", "score": 55}],
        },
    ]

    assert matching_rows(groups, min_score=60) == ["c"]
    assert pushdown_summary(groups, min_score=60) == {
        "total_groups": 2,
        "scanned_groups": ["g2"],
        "scanned_group_count": 1,
        "matching_rows": ["c"],
    }

import pytest

from point_lookups_vs_range_scans import (
    access_summary,
    choose_access_path,
    point_lookup_work,
    range_scan_work,
)


def test_range_scan_work_grows_with_matching_rows() -> None:
    assert point_lookup_work(3) == 4
    assert range_scan_work(3, 1) == 5
    assert range_scan_work(3, 20) == 24


def test_access_summary_prefers_point_for_single_match() -> None:
    summary = access_summary(index_height=4, matching_rows=1)

    assert summary["point_lookup_work"] == 5
    assert summary["range_scan_work"] == 6
    assert summary["recommended_path"] == "point-lookup"


def test_choose_access_path_rejects_unknown_shape() -> None:
    assert choose_access_path("point", matching_rows=1) == "point-lookup"
    assert choose_access_path("range", matching_rows=8) == "range-scan"

    with pytest.raises(ValueError):
        choose_access_path("prefix", matching_rows=3)

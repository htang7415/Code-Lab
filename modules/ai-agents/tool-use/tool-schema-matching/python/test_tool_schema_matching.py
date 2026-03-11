from __future__ import annotations

from tool_schema_matching import best_schema_match, schema_fields, schema_match_score


def test_tool_schema_matching_extracts_and_scores_fields() -> None:
    weather = {"properties": {"city": {}, "units": {}}}
    calendar = {"properties": {"date": {}, "title": {}}}
    assert schema_fields(weather) == ["city", "units"]
    assert schema_match_score(["city"], ["city", "units"]) == 1
    assert best_schema_match(["city"], {"weather": weather, "calendar": calendar}) == "weather"


def test_tool_schema_matching_returns_none_without_overlap() -> None:
    search = {"properties": {"query": {}}}
    assert best_schema_match(["city"], {"search": search}) is None

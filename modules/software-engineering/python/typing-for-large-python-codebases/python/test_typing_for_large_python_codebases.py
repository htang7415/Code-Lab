from __future__ import annotations

import pytest

from typing_for_large_python_codebases import missing_annotations, needs_protocol, typed_api_ready


def test_missing_annotations_reports_untyped_params_and_return_values() -> None:
    assert missing_annotations({"user_id": "str", "limit": None}, return_type="list[str]") == ["limit"]
    assert missing_annotations({"user_id": "str"}, return_type=None) == ["return"]


def test_typed_api_ready_requires_complete_boundary_annotations() -> None:
    assert typed_api_ready({"user_id": "str", "limit": "int"}, return_type="list[str]") is True
    assert typed_api_ready({"user_id": None}, return_type="list[str]") is False


def test_needs_protocol_when_multiple_implementations_share_a_boundary() -> None:
    assert needs_protocol(interface_methods=4, multiple_implementations=True) is True
    assert needs_protocol(interface_methods=1, multiple_implementations=True) is False

    with pytest.raises(ValueError):
        needs_protocol(interface_methods=-1, multiple_implementations=True)

from __future__ import annotations

import pytest

from prompt_structuring import build_messages, format_checklist


def test_prompt_structuring_builds_messages_with_optional_constraints() -> None:
    checklist = format_checklist(["answer in bullets", "cite sources"])
    assert checklist == "- answer in bullets\n- cite sources"
    messages = build_messages(
        system_prompt="You are careful.",
        user_prompt="Summarize the memo.",
        checklist=["answer in bullets", "cite sources"],
    )
    assert messages[0]["role"] == "system"
    assert messages[-1]["content"].startswith("Constraints:\n- answer in bullets")


def test_prompt_structuring_rejects_empty_core_messages() -> None:
    with pytest.raises(ValueError):
        build_messages("", "hello")
    with pytest.raises(ValueError):
        build_messages("system", "")

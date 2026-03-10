from __future__ import annotations


def format_checklist(items: list[str]) -> str:
    cleaned = [item.strip() for item in items if item.strip()]
    return "\n".join(f"- {item}" for item in cleaned)


def build_messages(
    system_prompt: str,
    user_prompt: str,
    checklist: list[str] | None = None,
) -> list[dict[str, str]]:
    if not system_prompt.strip():
        raise ValueError("system_prompt must be non-empty")
    if not user_prompt.strip():
        raise ValueError("user_prompt must be non-empty")

    messages = [
        {"role": "system", "content": system_prompt.strip()},
        {"role": "user", "content": user_prompt.strip()},
    ]
    if checklist:
        formatted = format_checklist(checklist)
        if formatted:
            messages.append(
                {
                    "role": "user",
                    "content": f"Constraints:\n{formatted}",
                }
            )
    return messages

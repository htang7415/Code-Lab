"""document_modeling - a small nested conversation document."""

from __future__ import annotations


def create_conversation_document(session_id: str, user_id: int) -> dict[str, object]:
    return {
        "session_id": session_id,
        "user_id": user_id,
        "messages": [],
    }


def append_message(
    document: dict[str, object],
    role: str,
    text: str,
    created_at: str,
    metadata: dict[str, object] | None = None,
) -> None:
    messages = document.setdefault("messages", [])
    assert isinstance(messages, list)
    messages.append(
        {
            "role": role,
            "text": text,
            "created_at": created_at,
            "metadata": metadata or {},
        }
    )


def latest_message_by_role(
    document: dict[str, object],
    role: str,
) -> dict[str, object] | None:
    messages = document.get("messages", [])
    assert isinstance(messages, list)
    for message in reversed(messages):
        if message["role"] == role:
            return message
    return None


def conversation_summary(document: dict[str, object]) -> dict[str, object]:
    messages = document.get("messages", [])
    assert isinstance(messages, list)
    roles = sorted({message["role"] for message in messages})
    return {
        "session_id": document["session_id"],
        "message_count": len(messages),
        "roles": roles,
    }

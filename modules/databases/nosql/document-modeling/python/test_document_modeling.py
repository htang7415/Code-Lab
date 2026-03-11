from document_modeling import (
    append_message,
    conversation_summary,
    create_conversation_document,
    latest_message_by_role,
)


def build_session() -> dict[str, object]:
    session = create_conversation_document("sess-1", 42)
    append_message(session, "user", "Find failed runs", "2026-03-11T10:00:00Z")
    append_message(
        session,
        "assistant",
        "I found three failed runs.",
        "2026-03-11T10:00:02Z",
    )
    append_message(session, "user", "Only show production", "2026-03-11T10:00:04Z")
    return session


def test_messages_stay_nested_in_order_inside_one_document() -> None:
    session = build_session()

    assert [message["role"] for message in session["messages"]] == [
        "user",
        "assistant",
        "user",
    ]


def test_latest_message_by_role_returns_the_most_recent_matching_message() -> None:
    session = build_session()

    assert latest_message_by_role(session, "assistant") == {
        "role": "assistant",
        "text": "I found three failed runs.",
        "created_at": "2026-03-11T10:00:02Z",
        "metadata": {},
    }


def test_conversation_summary_counts_messages_and_roles() -> None:
    session = build_session()

    assert conversation_summary(session) == {
        "session_id": "sess-1",
        "message_count": 3,
        "roles": ["assistant", "user"],
    }

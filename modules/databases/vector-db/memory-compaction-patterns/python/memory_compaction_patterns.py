"""memory_compaction_patterns - keep important memories raw and summarize the rest."""

from __future__ import annotations


def memory_score(
    memory: dict[str, object],
    now: int,
    recency_window: int = 3600,
) -> float:
    if memory.get("pinned"):
        return 1000.0 + float(memory.get("importance", 0.5))
    age = max(now - int(memory["created_at"]), 0)
    recency = max(0.0, 1.0 - (age / recency_window))
    importance = float(memory.get("importance", 0.5))
    return (0.7 * importance) + (0.3 * recency)


def raw_memory_ids(
    memories: list[dict[str, object]],
    now: int,
    keep_raw: int,
) -> list[str]:
    ranked = sorted(
        memories,
        key=lambda memory: (
            -memory_score(memory, now),
            -int(memory["created_at"]),
            str(memory["id"]),
        ),
    )
    return [str(memory["id"]) for memory in ranked[:keep_raw]]


def summary_text(memories: list[dict[str, object]]) -> str:
    ordered = sorted(memories, key=lambda memory: (int(memory["created_at"]), str(memory["id"])))
    return " | ".join(str(memory["text"]) for memory in ordered)


def compact_memories(
    memories: list[dict[str, object]],
    now: int,
    keep_raw: int,
) -> list[dict[str, object]]:
    kept_ids = set(raw_memory_ids(memories, now, keep_raw))
    kept_raw = [dict(memory) for memory in memories if str(memory["id"]) in kept_ids]

    grouped: dict[str, list[dict[str, object]]] = {}
    for memory in memories:
        if str(memory["id"]) in kept_ids:
            continue
        grouped.setdefault(str(memory.get("topic", "general")), []).append(memory)

    summaries: list[dict[str, object]] = []
    for topic, topic_memories in sorted(grouped.items()):
        summaries.append(
            {
                "id": f"summary:{topic}",
                "topic": topic,
                "text": f"Summary of {topic}: {summary_text(topic_memories)}",
                "created_at": max(int(memory["created_at"]) for memory in topic_memories),
                "importance": max(float(memory.get("importance", 0.5)) for memory in topic_memories),
                "kind": "summary",
            }
        )

    combined = kept_raw + summaries
    return sorted(combined, key=lambda memory: (int(memory["created_at"]), str(memory["id"])))

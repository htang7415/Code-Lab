from join_shapes import (
    create_connection,
    create_join_demo_tables,
    documents_without_chunks,
    inner_join_document_chunks,
    left_join_document_chunk_counts,
    seed_chunks,
    seed_documents,
)


def build_seeded_connection():
    conn = create_connection()
    create_join_demo_tables(conn)
    seed_documents(conn, [(1, "spec"), (2, "roadmap"), (3, "notes")])
    seed_chunks(
        conn,
        [
            (1, 0, "chunk a"),
            (1, 1, "chunk b"),
            (3, 0, "chunk c"),
        ],
    )
    return conn


def test_inner_join_returns_only_matching_parent_child_pairs() -> None:
    conn = build_seeded_connection()

    assert inner_join_document_chunks(conn) == [
        ("spec", "chunk a"),
        ("spec", "chunk b"),
        ("notes", "chunk c"),
    ]


def test_left_join_keeps_documents_that_have_zero_chunks() -> None:
    conn = build_seeded_connection()

    assert left_join_document_chunk_counts(conn) == [
        ("spec", 2),
        ("roadmap", 0),
        ("notes", 1),
    ]


def test_anti_join_finds_documents_without_children() -> None:
    conn = build_seeded_connection()

    assert documents_without_chunks(conn) == ["roadmap"]

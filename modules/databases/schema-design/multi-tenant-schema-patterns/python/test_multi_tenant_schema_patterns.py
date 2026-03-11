import sqlite3

import pytest

from multi_tenant_schema_patterns import (
    create_connection,
    create_multi_tenant_schema,
    document_titles_for_workspace,
    insert_chunk,
    insert_document,
    insert_workspace,
)


def build_seeded_connection():
    conn = create_connection()
    create_multi_tenant_schema(conn)
    team_a = insert_workspace(conn, "team-a")
    team_b = insert_workspace(conn, "team-b")
    doc_a = insert_document(conn, team_a, "spec")
    insert_document(conn, team_b, "spec")
    insert_chunk(conn, team_a, doc_a, 0, "chunk a")
    return conn, team_a, team_b, doc_a


def test_same_title_can_exist_in_different_tenants() -> None:
    conn, team_a, team_b, _ = build_seeded_connection()

    assert document_titles_for_workspace(conn, team_a) == ["spec"]
    assert document_titles_for_workspace(conn, team_b) == ["spec"]


def test_composite_foreign_key_blocks_cross_tenant_child_rows() -> None:
    conn, _, team_b, doc_a = build_seeded_connection()

    with pytest.raises(sqlite3.IntegrityError):
        insert_chunk(conn, team_b, doc_a, 0, "wrong tenant")


def test_workspace_filtered_query_returns_only_that_tenants_documents() -> None:
    conn, team_a, team_b, _ = build_seeded_connection()
    insert_document(conn, team_a, "roadmap")
    insert_document(conn, team_b, "playbook")

    assert document_titles_for_workspace(conn, team_a) == ["spec", "roadmap"]
    assert document_titles_for_workspace(conn, team_b) == ["spec", "playbook"]

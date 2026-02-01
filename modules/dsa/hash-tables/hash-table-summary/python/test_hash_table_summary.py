from hash_table_summary import hash_table_summary


def test_hash_table_summary_basic():
    result = hash_table_summary(["a", "b", "a", "c", "b", "a"])
    assert result == {"unique": 3, "most_common": "a", "max_count": 3}


def test_hash_table_summary_empty():
    assert hash_table_summary([]) == {"unique": 0, "most_common": None, "max_count": 0}

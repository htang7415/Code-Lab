from linked_list_basics import linked_list_basics


def test_linked_list_basics_non_empty():
    assert linked_list_basics([1, 2, 3]) == {
        "length": 3,
        "head": 1,
        "tail": 3,
    }


def test_linked_list_basics_empty():
    assert linked_list_basics([]) == {
        "length": 0,
        "head": None,
        "tail": None,
    }

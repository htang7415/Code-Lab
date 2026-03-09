from problem_1047_remove_all_adjacent_duplicates_in_string import Solution


def test_remove_duplicates_example():
    assert Solution().removeDuplicates("abbaca") == "ca"


def test_remove_duplicates_edge_none():
    assert Solution().removeDuplicates("abcd") == "abcd"


def test_remove_duplicates_tricky_cascade():
    assert Solution().removeDuplicates("azxxzy") == "ay"

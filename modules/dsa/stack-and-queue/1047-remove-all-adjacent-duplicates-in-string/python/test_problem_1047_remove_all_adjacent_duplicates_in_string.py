from problem_1047_remove_all_adjacent_duplicates_in_string import Solution


def test_remove_duplicates_basic():
    assert Solution().removeDuplicates("abbaca") == "ca"


def test_remove_duplicates_none():
    assert Solution().removeDuplicates("abcd") == "abcd"

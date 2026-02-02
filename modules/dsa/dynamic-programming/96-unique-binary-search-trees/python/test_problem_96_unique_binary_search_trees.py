from problem_96_unique_binary_search_trees import Solution


def test_unique_bst_basic():
    assert Solution().numTrees(3) == 5


def test_unique_bst_single():
    assert Solution().numTrees(1) == 1

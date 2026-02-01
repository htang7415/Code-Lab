from binary_search import Solution

def test_binary_search_found():
    assert Solution().search([-1, 0, 3, 5, 9, 12], 9) == 4

def test_binary_search_not_found():
    assert Solution().search([-1, 0, 3, 5, 9, 12], 2) == -1

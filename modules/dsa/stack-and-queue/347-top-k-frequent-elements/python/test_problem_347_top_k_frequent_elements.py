from problem_347_top_k_frequent_elements import Solution


def test_top_k_example():
    result = Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)
    assert set(result) == {1, 2}


def test_top_k_edge_single():
    assert Solution().topKFrequent([1], 1) == [1]


def test_top_k_tricky_negative_values():
    result = Solution().topKFrequent([4, 1, -1, 2, -1, 2, 3], 2)
    assert set(result) == {-1, 2}

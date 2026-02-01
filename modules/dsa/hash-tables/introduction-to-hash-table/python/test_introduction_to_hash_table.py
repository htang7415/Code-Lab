from introduction_to_hash_table import frequency_map


def test_frequency_map_basic():
    assert frequency_map([1, 2, 2, 3, 3, 3]) == {1: 1, 2: 2, 3: 3}


def test_frequency_map_empty():
    assert frequency_map([]) == {}

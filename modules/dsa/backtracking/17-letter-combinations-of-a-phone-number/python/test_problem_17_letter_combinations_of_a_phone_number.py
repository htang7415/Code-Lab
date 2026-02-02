from problem_17_letter_combinations_of_a_phone_number import Solution


def test_letter_combinations_basic():
    result = Solution().letterCombinations("23")
    assert set(result) == {"ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"}


def test_letter_combinations_empty():
    assert Solution().letterCombinations("") == []

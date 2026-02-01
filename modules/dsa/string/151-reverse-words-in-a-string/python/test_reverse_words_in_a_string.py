from reverse_words_in_a_string import Solution

def test_reverse_words_basic():
    assert Solution().reverseWords("the sky is blue") == "blue is sky the"

def test_reverse_words_extra_spaces():
    assert Solution().reverseWords("  hello   world  ") == "world hello"

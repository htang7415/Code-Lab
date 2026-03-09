from speculative_decoding import speculative_decode_step


def test_speculative_decode_step_accepts_prefix_until_mismatch():
    assert speculative_decode_step([1, 2, 3], [1, 2, 4, 5]) == [1, 2, 4]


def test_speculative_decode_step_accepts_full_draft_and_next_target_token():
    assert speculative_decode_step([1, 2], [1, 2, 7]) == [1, 2, 7]

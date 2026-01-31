from batch_vs_realtime import choose_mode


def test_choose_mode():
    assert choose_mode(1) == "realtime"
    assert choose_mode(8) == "batch"

from ppo import clip_ratio


def test_clip_ratio():
    assert clip_ratio(1.5, 0.2) == 1.2

from offline_online_inference import is_online


def test_is_online():
    assert is_online(50.0)
    assert not is_online(500.0)

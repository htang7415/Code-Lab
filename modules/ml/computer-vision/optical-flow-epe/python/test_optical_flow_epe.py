from optical_flow_epe import epe


def test_epe():
    assert epe((0.0, 0.0), (3.0, 4.0)) == 5.0

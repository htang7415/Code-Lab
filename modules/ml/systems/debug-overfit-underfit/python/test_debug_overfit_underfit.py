from debug_overfit_underfit import diagnose


def test_diagnose():
    assert diagnose(0.2, 0.5) == "overfit"

from model_selection import choose_model


def test_choose_model():
    assert choose_model("speed") == "gan"

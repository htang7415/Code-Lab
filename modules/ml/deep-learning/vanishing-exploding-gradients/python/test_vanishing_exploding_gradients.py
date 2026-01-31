from vanishing_exploding_gradients import gradient_chain


def test_gradient_chain():
    assert gradient_chain([0.5, 0.5]) == 0.25

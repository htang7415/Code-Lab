from mdp import transition_prob


def test_transition_prob():
    transitions = {(0, 1): {2: 0.8}}
    assert transition_prob(transitions, 0, 1, 2) == 0.8

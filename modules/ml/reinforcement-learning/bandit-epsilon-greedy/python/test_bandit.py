from bandit import EpsilonGreedyBandit


def test_initial_values():
    agent = EpsilonGreedyBandit(k=3)
    assert agent.q_values == [0.0, 0.0, 0.0]
    assert agent.counts == [0, 0, 0]


def test_update_single_arm():
    agent = EpsilonGreedyBandit(k=2, seed=0)
    agent.update(0, 1.0)
    assert agent.q_values[0] == 1.0
    assert agent.counts[0] == 1
    agent.update(0, 3.0)
    assert agent.q_values[0] == 2.0  # mean of 1 and 3
    assert agent.counts[0] == 2


def test_greedy_selects_best():
    agent = EpsilonGreedyBandit(k=3, epsilon=0.0, seed=42)
    agent.q_values = [1.0, 5.0, 3.0]
    # With epsilon=0, should always pick arm 1
    for _ in range(10):
        assert agent.select_arm() == 1


def test_exploration_happens():
    agent = EpsilonGreedyBandit(k=3, epsilon=1.0, seed=42)
    agent.q_values = [0.0, 100.0, 0.0]
    # With epsilon=1, should explore randomly — not always arm 1
    arms = {agent.select_arm() for _ in range(50)}
    assert len(arms) > 1  # at least two different arms chosen

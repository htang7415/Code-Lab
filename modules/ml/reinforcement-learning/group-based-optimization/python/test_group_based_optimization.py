import math

from group_based_optimization import (
    group_advantages,
    grpo_objective,
    gspo_objective,
)


def test_group_advantages_centered():
    rewards = [0.0, 1.0]
    adv = group_advantages(rewards)
    assert len(adv) == 2
    assert abs(sum(adv)) < 1e-9
    assert adv[0] == -adv[1]


def test_grpo_gspo_objectives_match_expected():
    rewards = [0.0, 1.0]
    old_logps = [[-0.1, -0.1], [-0.2, -0.2]]
    new_logps = [[-0.2, -0.2], [-0.2, -0.2]]

    gspo = gspo_objective(old_logps, new_logps, rewards)
    grpo = grpo_objective(old_logps, new_logps, rewards)

    seq_ratio = math.exp((-0.2 + 0.1) + (-0.2 + 0.1))
    token_ratio = math.exp(-0.1)
    expected_gspo = (-seq_ratio + 1.0) / 2.0
    expected_grpo = (-token_ratio + 1.0) / 2.0

    assert abs(gspo - expected_gspo) < 1e-6
    assert abs(grpo - expected_grpo) < 1e-6

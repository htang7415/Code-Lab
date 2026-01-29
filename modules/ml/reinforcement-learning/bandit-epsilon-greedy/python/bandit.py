"""Epsilon-greedy multi-armed bandit."""

import random
from typing import List


class EpsilonGreedyBandit:
    """Epsilon-greedy agent for the multi-armed bandit problem."""

    def __init__(self, k: int, epsilon: float = 0.1, seed: int | None = None):
        """
        Args:
            k: number of arms
            epsilon: exploration probability (0 to 1)
            seed: optional random seed for reproducibility
        """
        self.k = k
        self.epsilon = epsilon
        self.q_values: List[float] = [0.0] * k  # estimated action values
        self.counts: List[int] = [0] * k  # pull counts per arm
        self._rng = random.Random(seed)

    def select_arm(self) -> int:
        """Choose an arm using epsilon-greedy strategy."""
        if self._rng.random() < self.epsilon:
            return self._rng.randint(0, self.k - 1)
        # Greedy: pick arm with highest Q (break ties randomly)
        max_q = max(self.q_values)
        best_arms = [a for a in range(self.k) if self.q_values[a] == max_q]
        return self._rng.choice(best_arms)

    def update(self, arm: int, reward: float) -> None:
        """Update the value estimate for the chosen arm."""
        self.counts[arm] += 1
        # Incremental mean update
        self.q_values[arm] += (reward - self.q_values[arm]) / self.counts[arm]

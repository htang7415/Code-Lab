def transition_prob(transitions: dict[tuple[int, int], dict[int, float]], s: int, a: int, s_next: int) -> float:
    return transitions.get((s, a), {}).get(s_next, 0.0)

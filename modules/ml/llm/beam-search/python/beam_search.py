from __future__ import annotations


def beam_search_step(
    beams: list[tuple[list[int], float]],
    next_token_log_probs: list[list[float]],
    beam_width: int,
) -> list[tuple[list[int], float]]:
    if len(beams) != len(next_token_log_probs):
        raise ValueError("beams and next_token_log_probs must have the same length")
    if beam_width <= 0:
        raise ValueError("beam_width must be positive")
    if not beams:
        return []

    candidates: list[tuple[list[int], float]] = []
    for (tokens, score), token_scores in zip(beams, next_token_log_probs):
        for token_id, token_log_prob in enumerate(token_scores):
            candidates.append((tokens + [token_id], score + token_log_prob))

    candidates.sort(key=lambda item: item[1], reverse=True)
    return candidates[:beam_width]

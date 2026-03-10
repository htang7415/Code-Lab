from __future__ import annotations


def _validate_binary_flags(correct: list[int]) -> None:
    if any(value not in (0, 1) for value in correct):
        raise ValueError("correct must contain only 0 or 1")


def reasoning_accuracy(correct: list[int]) -> float:
    _validate_binary_flags(correct)
    return sum(correct) / len(correct) if correct else 0.0


def successes_per_1k_tokens(correct: list[int], token_costs: list[int]) -> float:
    _validate_binary_flags(correct)
    if len(correct) != len(token_costs):
        raise ValueError("correct and token_costs must have the same length")
    if any(cost <= 0 for cost in token_costs):
        raise ValueError("token_costs must be positive")
    total_tokens = sum(token_costs)
    if total_tokens == 0:
        return 0.0
    return 1000.0 * sum(correct) / total_tokens


def majority_vote_gain(single_success_rate: float, vote_success_rate: float) -> float:
    if not 0.0 <= single_success_rate <= 1.0:
        raise ValueError("single_success_rate must satisfy 0 <= value <= 1")
    if not 0.0 <= vote_success_rate <= 1.0:
        raise ValueError("vote_success_rate must satisfy 0 <= value <= 1")
    return vote_success_rate - single_success_rate


def success_under_token_budget(correct: list[int], token_costs: list[int], max_tokens: int) -> float:
    _validate_binary_flags(correct)
    if len(correct) != len(token_costs):
        raise ValueError("correct and token_costs must have the same length")
    if any(cost <= 0 for cost in token_costs):
        raise ValueError("token_costs must be positive")
    if max_tokens <= 0:
        raise ValueError("max_tokens must be positive")

    budgeted = [flag for flag, cost in zip(correct, token_costs) if cost <= max_tokens]
    return sum(budgeted) / len(budgeted) if budgeted else 0.0

from __future__ import annotations

from collections.abc import Callable


Candidate = dict[str, int | str]
Strategy = Callable[[list[Candidate]], Candidate]


def lowest_latency(candidates: list[Candidate]) -> Candidate:
    return min(candidates, key=lambda candidate: (int(candidate["latency_ms"]), int(candidate["monthly_cost"])))


def lowest_cost(candidates: list[Candidate]) -> Candidate:
    return min(candidates, key=lambda candidate: (int(candidate["monthly_cost"]), int(candidate["latency_ms"])))


def select_region(candidates: list[Candidate], strategy: Strategy) -> str:
    return str(strategy(candidates)["name"])

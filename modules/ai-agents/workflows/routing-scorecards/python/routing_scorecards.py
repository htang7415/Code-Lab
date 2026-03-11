from __future__ import annotations


def route_score(route_signals: dict[str, float], signal_weights: dict[str, float]) -> float:
    if not route_signals:
        raise ValueError("route_signals must be non-empty")
    if not signal_weights:
        raise ValueError("signal_weights must be non-empty")

    weighted_sum = 0.0
    total_weight = 0.0
    for signal_name, score in route_signals.items():
        cleaned_signal = signal_name.strip()
        if not cleaned_signal:
            raise ValueError("signal names must be non-empty")
        if cleaned_signal not in signal_weights:
            raise ValueError(f"missing weight for signal: {cleaned_signal}")
        if not 0.0 <= score <= 1.0:
            raise ValueError("signal scores must satisfy 0 <= value <= 1")

        weight = signal_weights[cleaned_signal]
        if weight <= 0.0:
            raise ValueError("signal weights must be positive")
        weighted_sum += score * weight
        total_weight += weight

    return weighted_sum / total_weight


def score_routes(
    route_to_signals: dict[str, dict[str, float]],
    signal_weights: dict[str, float],
) -> list[dict[str, object]]:
    if not route_to_signals:
        raise ValueError("route_to_signals must be non-empty")

    scored_routes: list[dict[str, object]] = []
    for route_name, route_signals in route_to_signals.items():
        cleaned_route = route_name.strip()
        if not cleaned_route:
            raise ValueError("route names must be non-empty")
        scored_routes.append(
            {
                "route": cleaned_route,
                "score": route_score(route_signals, signal_weights),
            }
        )

    return sorted(
        scored_routes,
        key=lambda item: (-float(item["score"]), str(item["route"])),
    )


def scorecard_route(
    route_to_signals: dict[str, dict[str, float]],
    signal_weights: dict[str, float],
    min_score: float,
    min_margin: float = 0.0,
) -> str:
    if not 0.0 <= min_score <= 1.0:
        raise ValueError("min_score must satisfy 0 <= value <= 1")
    if min_margin < 0.0:
        raise ValueError("min_margin must be non-negative")

    ranked = score_routes(route_to_signals, signal_weights)
    top_score = float(ranked[0]["score"])
    if top_score < min_score:
        return "review"

    if len(ranked) > 1:
        next_score = float(ranked[1]["score"])
        if top_score - next_score < min_margin:
            return "review"

    return str(ranked[0]["route"])

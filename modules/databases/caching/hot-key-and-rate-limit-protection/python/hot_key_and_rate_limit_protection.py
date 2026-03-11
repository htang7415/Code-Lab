"""hot_key_and_rate_limit_protection - detect hot keys and throttle origin load."""

from __future__ import annotations


def validate_hot_threshold(threshold: int) -> None:
    if threshold <= 0:
        raise ValueError("threshold must be positive")


def validate_rate_limit(max_requests: int, window_seconds: int) -> None:
    if max_requests <= 0:
        raise ValueError("max_requests must be positive")
    if window_seconds <= 0:
        raise ValueError("window_seconds must be positive")


def hot_keys(requests: list[str], threshold: int) -> list[str]:
    validate_hot_threshold(threshold)
    counts: dict[str, int] = {}
    for key in requests:
        counts[key] = counts.get(key, 0) + 1
    return sorted(key for key, count in counts.items() if count >= threshold)


def allow_request(
    state: dict[tuple[str, str], list[int]],
    actor_id: str,
    key: str,
    now: int,
    max_requests: int,
    window_seconds: int,
) -> bool:
    validate_rate_limit(max_requests, window_seconds)
    bucket = (actor_id, key)
    recent = [timestamp for timestamp in state.get(bucket, []) if now - timestamp < window_seconds]
    if len(recent) >= max_requests:
        state[bucket] = recent
        return False
    recent.append(now)
    state[bucket] = recent
    return True


def protected_origin_requests(
    requests: list[dict[str, object]],
    hot_threshold: int,
    max_requests: int,
    window_seconds: int,
) -> list[bool]:
    validate_hot_threshold(hot_threshold)
    validate_rate_limit(max_requests, window_seconds)
    counts: dict[str, int] = {}
    state: dict[tuple[str, str], list[int]] = {}
    allowed: list[bool] = []

    for request in requests:
        actor_id = str(request["actor_id"])
        key = str(request["key"])
        now = int(request["now"])
        counts[key] = counts.get(key, 0) + 1

        if counts[key] < hot_threshold:
            allowed.append(True)
            continue

        allowed.append(
            allow_request(
                state,
                actor_id=actor_id,
                key=key,
                now=now,
                max_requests=max_requests,
                window_seconds=window_seconds,
            )
        )
    return allowed

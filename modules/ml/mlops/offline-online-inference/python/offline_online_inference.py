def is_online(latency_ms: float, threshold_ms: float = 100.0) -> bool:
    return latency_ms <= threshold_ms

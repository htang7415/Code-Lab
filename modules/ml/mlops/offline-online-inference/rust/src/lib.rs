pub fn is_online(latency_ms: f64, threshold_ms: f64) -> bool {
    latency_ms <= threshold_ms
}

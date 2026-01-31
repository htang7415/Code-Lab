pub fn update_value(q: f64, n: i32, reward: f64) -> f64 {
    q + (reward - q) / n as f64
}

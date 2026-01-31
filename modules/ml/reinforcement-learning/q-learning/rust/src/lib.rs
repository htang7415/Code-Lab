pub fn q_update(q: f64, reward: f64, next_max: f64, alpha: f64, gamma: f64) -> f64 {
    q + alpha * (reward + gamma * next_max - q)
}

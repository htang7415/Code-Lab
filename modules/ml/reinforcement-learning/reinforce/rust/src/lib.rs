pub fn reinforce_update(grad_logp: f64, reward: f64, lr: f64) -> f64 {
    lr * reward * grad_logp
}

pub fn beta_posterior(alpha: f64, beta: f64, successes: i32, failures: i32) -> (f64, f64) {
    (alpha + successes as f64, beta + failures as f64)
}

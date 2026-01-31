pub fn exp_decay(lr: f64, k: f64, t: f64) -> f64 {
    lr * (-k * t).exp()
}

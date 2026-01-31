pub fn step_decay(lr: f64, step: i32, gamma: f64, t: i32) -> f64 {
    let k = t / step;
    lr * gamma.powi(k)
}

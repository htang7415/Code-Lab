pub fn cosine_decay(lr: f64, t: i32, t_max: i32) -> f64 {
    lr * 0.5 * (1.0 + (std::f64::consts::PI * t as f64 / t_max as f64).cos())
}

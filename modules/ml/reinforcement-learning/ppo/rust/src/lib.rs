pub fn clip_ratio(ratio: f64, eps: f64) -> f64 {
    let lower = 1.0 - eps;
    let upper = 1.0 + eps;
    ratio.max(lower).min(upper)
}

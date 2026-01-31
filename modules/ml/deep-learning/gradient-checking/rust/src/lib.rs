pub fn grad_check(f: fn(f64) -> f64, x: f64, eps: f64) -> f64 {
    (f(x + eps) - f(x - eps)) / (2.0 * eps)
}

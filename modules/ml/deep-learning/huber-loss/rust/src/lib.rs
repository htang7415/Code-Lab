pub fn huber(y: f64, y_hat: f64, delta: f64) -> f64 {
    let e = y - y_hat;
    if e.abs() <= delta {
        0.5 * e * e
    } else {
        delta * (e.abs() - 0.5 * delta)
    }
}

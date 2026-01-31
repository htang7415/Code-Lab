pub fn gradients_ok(grads: &[f64]) -> bool {
    if grads.iter().any(|g| g.is_nan()) { return false; }
    grads.iter().any(|g| g.abs() > 0.0)
}

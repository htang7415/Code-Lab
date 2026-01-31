pub fn dead_relu_fraction(values: &[f64]) -> f64 {
    if values.is_empty() {
        return 0.0;
    }
    let dead = values.iter().filter(|v| **v <= 0.0).count();
    dead as f64 / values.len() as f64
}

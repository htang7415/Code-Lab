pub fn normalize_probs(values: &[f64]) -> Vec<f64> {
    let sum: f64 = values.iter().sum();
    values.iter().map(|v| v / sum).collect()
}

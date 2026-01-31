pub fn missing_rate(values: &[Option<f64>]) -> f64 {
    let missing = values.iter().filter(|v| v.is_none()).count();
    missing as f64 / values.len() as f64
}

pub fn has_nan(values: &[f64]) -> bool {
    values.iter().any(|v| v.is_nan())
}

pub fn normalize(values: &[f64]) -> Vec<f64> {
    let mean: f64 = values.iter().sum::<f64>() / values.len() as f64;
    let var: f64 = values.iter().map(|v| (v - mean).powi(2)).sum::<f64>() / values.len() as f64;
    let std = if var > 0.0 { var.sqrt() } else { 1.0 };
    values.iter().map(|v| (v - mean) / std).collect()
}

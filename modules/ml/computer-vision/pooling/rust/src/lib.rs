pub fn max_pool(window: &[f64]) -> f64 {
    window.iter().copied().fold(f64::NEG_INFINITY, f64::max)
}

pub fn avg_pool(window: &[f64]) -> f64 {
    window.iter().sum::<f64>() / window.len() as f64
}

pub fn mae(y: &[f64], y_hat: &[f64]) -> f64 {
    let sum: f64 = y.iter().zip(y_hat.iter()).map(|(a, b)| (a - b).abs()).sum();
    sum / y.len() as f64
}

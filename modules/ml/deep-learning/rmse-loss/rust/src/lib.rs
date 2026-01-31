pub fn rmse(y: &[f64], y_hat: &[f64]) -> f64 {
    let sum: f64 = y.iter().zip(y_hat.iter()).map(|(a, b)| (a - b).powi(2)).sum();
    (sum / y.len() as f64).sqrt()
}

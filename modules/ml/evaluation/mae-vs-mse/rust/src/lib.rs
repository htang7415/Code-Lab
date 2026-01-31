pub fn mae_mse(y: &[f64], y_hat: &[f64]) -> (f64, f64) {
    let mae = y.iter().zip(y_hat.iter()).map(|(a, b)| (a - b).abs()).sum::<f64>() / y.len() as f64;
    let mse = y.iter().zip(y_hat.iter()).map(|(a, b)| (a - b).powi(2)).sum::<f64>() / y.len() as f64;
    (mae, mse)
}

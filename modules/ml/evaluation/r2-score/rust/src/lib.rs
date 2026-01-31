pub fn r2_score(y: &[f64], y_hat: &[f64]) -> f64 {
    let mean: f64 = y.iter().sum::<f64>() / y.len() as f64;
    let ss_res: f64 = y.iter().zip(y_hat.iter()).map(|(a, b)| (a - b).powi(2)).sum();
    let ss_tot: f64 = y.iter().map(|a| (a - mean).powi(2)).sum();
    if ss_tot > 0.0 { 1.0 - ss_res / ss_tot } else { 0.0 }
}

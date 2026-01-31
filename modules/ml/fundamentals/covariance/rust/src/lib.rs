pub fn covariance(x: &[f64], y: &[f64]) -> f64 {
    let mean_x: f64 = x.iter().sum::<f64>() / x.len() as f64;
    let mean_y: f64 = y.iter().sum::<f64>() / y.len() as f64;
    x.iter()
        .zip(y.iter())
        .map(|(a, b)| (a - mean_x) * (b - mean_y))
        .sum::<f64>()
        / x.len() as f64
}

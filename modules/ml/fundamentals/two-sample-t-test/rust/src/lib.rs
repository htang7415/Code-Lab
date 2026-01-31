pub fn t_stat(x: &[f64], y: &[f64]) -> f64 {
    let m1: f64 = x.iter().sum::<f64>() / x.len() as f64;
    let m2: f64 = y.iter().sum::<f64>() / y.len() as f64;
    let v1: f64 = x.iter().map(|v| (v - m1).powi(2)).sum::<f64>() / (x.len() as f64 - 1.0);
    let v2: f64 = y.iter().map(|v| (v - m2).powi(2)).sum::<f64>() / (y.len() as f64 - 1.0);
    (m1 - m2) / (v1 / x.len() as f64 + v2 / y.len() as f64).sqrt()
}

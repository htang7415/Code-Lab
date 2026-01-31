pub fn batchnorm(x: &[f64], eps: f64) -> Vec<f64> {
    let mean: f64 = x.iter().sum::<f64>() / x.len() as f64;
    let var: f64 = x.iter().map(|v| (v - mean).powi(2)).sum::<f64>() / x.len() as f64;
    x.iter().map(|v| (v - mean) / (var + eps).sqrt()).collect()
}

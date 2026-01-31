pub fn rmsnorm(x: &[f64], eps: f64) -> Vec<f64> {
    let rms = (x.iter().map(|v| v * v).sum::<f64>() / x.len() as f64 + eps).sqrt();
    x.iter().map(|v| v / rms).collect()
}

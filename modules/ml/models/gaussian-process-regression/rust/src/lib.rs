pub fn rbf_kernel(x: &[f64], y: &[f64], length_scale: f64) -> f64 {
    let dist2: f64 = x.iter().zip(y.iter()).map(|(a, b)| (a - b).powi(2)).sum();
    (-dist2 / (2.0 * length_scale * length_scale)).exp()
}

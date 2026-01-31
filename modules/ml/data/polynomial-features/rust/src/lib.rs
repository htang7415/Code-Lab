pub fn poly_features(x: f64, degree: usize) -> Vec<f64> {
    (1..=degree).map(|d| x.powi(d as i32)).collect()
}

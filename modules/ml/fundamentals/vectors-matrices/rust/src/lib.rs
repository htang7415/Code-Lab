pub fn matvec(a: &[Vec<f64>], x: &[f64]) -> Vec<f64> {
    a.iter().map(|row| row.iter().zip(x.iter()).map(|(ai, xi)| ai * xi).sum()).collect()
}

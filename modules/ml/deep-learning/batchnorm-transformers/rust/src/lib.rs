pub fn batch_stats(matrix: &[Vec<f64>]) -> (f64, f64) {
    let mut values = Vec::new();
    for row in matrix {
        for v in row {
            values.push(*v);
        }
    }
    let mean: f64 = values.iter().sum::<f64>() / values.len() as f64;
    let var: f64 = values.iter().map(|v| (v - mean).powi(2)).sum::<f64>() / values.len() as f64;
    (mean, var)
}

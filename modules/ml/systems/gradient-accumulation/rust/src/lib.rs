pub fn accumulate(grads: &[Vec<f64>]) -> Vec<f64> {
    if grads.is_empty() { return Vec::new(); }
    let mut total = vec![0.0; grads[0].len()];
    for g in grads {
        for i in 0..g.len() {
            total[i] += g[i];
        }
    }
    total
}

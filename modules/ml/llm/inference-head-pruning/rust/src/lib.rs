pub fn prune_heads(weights: &[Vec<f64>], keep: &[usize], head_dim: usize) -> Vec<Vec<f64>> {
    let mut out = Vec::with_capacity(weights.len());
    for row in weights {
        let mut new_row = Vec::new();
        for &h in keep {
            let start = h * head_dim;
            let end = start + head_dim;
            new_row.extend_from_slice(&row[start..end]);
        }
        out.push(new_row);
    }
    out
}

pub fn groupnorm(x: &[f64], groups: usize, eps: f64) -> Vec<f64> {
    let size = x.len();
    let group_size = size / groups;
    let mut out = Vec::with_capacity(size);
    for g in 0..groups {
        let start = g * group_size;
        let end = start + group_size;
        let chunk = &x[start..end];
        let mean: f64 = chunk.iter().sum::<f64>() / chunk.len() as f64;
        let var: f64 = chunk.iter().map(|v| (v - mean).powi(2)).sum::<f64>() / chunk.len() as f64;
        out.extend(chunk.iter().map(|v| (v - mean) / (var + eps).sqrt()));
    }
    out
}

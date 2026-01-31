pub fn moe_combine(experts: &[Vec<f64>], gates: &[f64], k: usize) -> Vec<f64> {
    let mut pairs: Vec<(usize, f64)> = gates.iter().copied().enumerate().collect();
    pairs.sort_by(|a, b| b.1.partial_cmp(&a.1).unwrap());
    let top = &pairs[..k];
    let total: f64 = top.iter().map(|(_, s)| *s).sum();
    let mut out = vec![0.0; experts[0].len()];
    for (idx, score) in top {
        let weight = score / total;
        for j in 0..experts[*idx].len() {
            out[j] += weight * experts[*idx][j];
        }
    }
    out
}

pub fn cross_entropy(logits: &[f64], target: usize) -> f64 {
    let m = logits.iter().copied().fold(f64::NEG_INFINITY, f64::max);
    let exps: Vec<f64> = logits.iter().map(|x| (x - m).exp()).collect();
    let sum: f64 = exps.iter().sum();
    let prob = exps[target] / sum;
    -prob.ln()
}

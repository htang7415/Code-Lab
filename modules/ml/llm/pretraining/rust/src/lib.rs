pub fn next_token_loss(logits: &[Vec<f64>], targets: &[usize]) -> f64 {
    let mut total = 0.0;
    for (row, &tgt) in logits.iter().zip(targets.iter()) {
        let m = row.iter().copied().fold(f64::NEG_INFINITY, f64::max);
        let exps: Vec<f64> = row.iter().map(|x| (x - m).exp()).collect();
        let sum: f64 = exps.iter().sum();
        let prob = exps[tgt] / sum;
        total += -prob.ln();
    }
    total / targets.len() as f64
}

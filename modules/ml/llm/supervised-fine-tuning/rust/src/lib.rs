pub fn sft_loss(logits: &[Vec<f64>], targets: &[usize], mask: &[u8]) -> f64 {
    let mut total = 0.0;
    let mut count = 0;
    for ((row, &tgt), &keep) in logits.iter().zip(targets.iter()).zip(mask.iter()) {
        if keep == 0 {
            continue;
        }
        let m = row.iter().copied().fold(f64::NEG_INFINITY, f64::max);
        let exps: Vec<f64> = row.iter().map(|x| (x - m).exp()).collect();
        let sum: f64 = exps.iter().sum();
        let prob = exps[tgt] / sum;
        total += -prob.ln();
        count += 1;
    }
    if count == 0 { 0.0 } else { total / count as f64 }
}

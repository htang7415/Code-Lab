fn softmax(logits: &[f64], temp: f64) -> Vec<f64> {
    let m = logits.iter().copied().fold(f64::NEG_INFINITY, f64::max);
    let exps: Vec<f64> = logits.iter().map(|x| ((x - m) / temp).exp()).collect();
    let sum: f64 = exps.iter().sum();
    exps.iter().map(|e| e / sum).collect()
}

pub fn distill_loss(student: &[f64], teacher: &[f64], temp: f64) -> f64 {
    let ps = softmax(student, temp);
    let pt = softmax(teacher, temp);
    let mut loss = 0.0;
    for (p_s, p_t) in ps.iter().zip(pt.iter()) {
        if *p_t > 0.0 && *p_s > 0.0 {
            loss += p_t * (p_t / p_s).ln();
        }
    }
    loss
}

pub fn softmax(row: &[f64]) -> Vec<f64> {
    let m = row.iter().copied().fold(f64::NEG_INFINITY, f64::max);
    let exps: Vec<f64> = row.iter().map(|x| (x - m).exp()).collect();
    let sum: f64 = exps.iter().sum();
    exps.iter().map(|e| e / sum).collect()
}

pub fn softplus(x: f64) -> f64 {
    (1.0 + x.exp()).ln()
}

pub fn softsign(x: f64) -> f64 {
    x / (1.0 + x.abs())
}

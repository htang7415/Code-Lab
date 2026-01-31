pub fn l1_penalty(weights: &[f64], lam: f64) -> f64 {
    lam * weights.iter().map(|w| w.abs()).sum::<f64>()
}

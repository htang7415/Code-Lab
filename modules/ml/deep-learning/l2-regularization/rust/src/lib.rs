pub fn l2_penalty(weights: &[f64], lam: f64) -> f64 {
    lam * weights.iter().map(|w| w * w).sum::<f64>()
}

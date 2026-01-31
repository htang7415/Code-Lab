pub fn update_weights(weights: &[f64], errors: &[i32], alpha: f64) -> Vec<f64> {
    let mut updated: Vec<f64> = weights
        .iter()
        .zip(errors.iter())
        .map(|(w, e)| w * (alpha * (*e as f64)).exp())
        .collect();
    let sum: f64 = updated.iter().sum();
    for w in updated.iter_mut() {
        *w /= sum;
    }
    updated
}

pub fn scale_gradients(grads: &[f64], scale: f64) -> Vec<f64> {
    grads.iter().map(|g| g * scale).collect()
}

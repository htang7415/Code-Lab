pub fn clip_norm(grad: &[f64], clip: f64) -> Vec<f64> {
    let norm = grad.iter().map(|g| g * g).sum::<f64>().sqrt();
    if norm == 0.0 || norm <= clip {
        return grad.to_vec();
    }
    let scale = clip / norm;
    grad.iter().map(|g| g * scale).collect()
}

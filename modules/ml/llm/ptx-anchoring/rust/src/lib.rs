pub fn anchored_loss(align_loss: f64, ptx_loss: f64, alpha: f64) -> f64 {
    (1.0 - alpha) * align_loss + alpha * ptx_loss
}

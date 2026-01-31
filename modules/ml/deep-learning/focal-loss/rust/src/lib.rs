pub fn focal_loss(p: f64, gamma: f64) -> f64 {
    -((1.0 - p).powf(gamma)) * p.ln()
}

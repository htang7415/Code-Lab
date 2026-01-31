pub fn add_noise(x: f64, noise: f64, alpha: f64) -> f64 {
    alpha.sqrt() * x + (1.0 - alpha).sqrt() * noise
}

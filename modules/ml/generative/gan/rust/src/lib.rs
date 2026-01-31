pub fn gan_loss(d_real: f64, d_fake: f64) -> f64 {
    -(d_real.ln()) - (1.0 - d_fake).ln()
}

pub fn elbo(recon: f64, kl: f64) -> f64 {
    recon - kl
}

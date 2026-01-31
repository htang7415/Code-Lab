pub fn dpo_loss(delta_logp: f64, delta_logp_ref: f64, beta: f64) -> f64 {
    let diff = beta * (delta_logp - delta_logp_ref);
    -1.0 / (1.0 + (-diff).exp()).ln()
}

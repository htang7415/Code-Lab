pub fn reward_model_loss(chosen: f64, rejected: f64) -> f64 {
    let diff = chosen - rejected;
    -1.0 / (1.0 + (-diff).exp()).ln()
}

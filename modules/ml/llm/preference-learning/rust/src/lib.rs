pub fn preference_loss(score_chosen: f64, score_rejected: f64) -> f64 {
    let diff = score_chosen - score_rejected;
    -1.0 / (1.0 + (-diff).exp()).ln()
}

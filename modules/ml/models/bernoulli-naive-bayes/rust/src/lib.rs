pub fn bernoulli_log_likelihood(x: &[i32], prob: &[f64]) -> f64 {
    let mut ll = 0.0;
    for (&xi, &p) in x.iter().zip(prob.iter()) {
        ll += (xi as f64) * p.ln() + (1.0 - xi as f64) * (1.0 - p).ln();
    }
    ll
}

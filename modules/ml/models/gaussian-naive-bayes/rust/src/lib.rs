pub fn gaussian_log_likelihood(x: &[f64], mean: &[f64], var: &[f64]) -> f64 {
    let mut ll = 0.0;
    for ((xi, mu), v) in x.iter().zip(mean.iter()).zip(var.iter()) {
        ll += -0.5 * ((2.0 * std::f64::consts::PI * v).ln() + (xi - mu).powi(2) / v);
    }
    ll
}

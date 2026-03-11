pub fn t_stat(x: &[f64], y: &[f64]) -> f64 {
    assert!(
        x.len() >= 2 && y.len() >= 2,
        "each sample must contain at least 2 observations"
    );

    let m1: f64 = x.iter().sum::<f64>() / x.len() as f64;
    let m2: f64 = y.iter().sum::<f64>() / y.len() as f64;
    let v1: f64 = x.iter().map(|v| (v - m1).powi(2)).sum::<f64>() / (x.len() as f64 - 1.0);
    let v2: f64 = y.iter().map(|v| (v - m2).powi(2)).sum::<f64>() / (y.len() as f64 - 1.0);
    let denom = (v1 / x.len() as f64 + v2 / y.len() as f64).sqrt();
    if denom == 0.0 {
        if m1 == m2 {
            0.0
        } else if m1 < m2 {
            f64::NEG_INFINITY
        } else {
            f64::INFINITY
        }
    } else {
        (m1 - m2) / denom
    }
}

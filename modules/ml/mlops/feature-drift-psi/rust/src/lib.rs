pub fn psi(expected: &[f64], actual: &[f64]) -> f64 {
    let mut total = 0.0;
    for (&e, &a) in expected.iter().zip(actual.iter()) {
        if e > 0.0 && a > 0.0 {
            total += (a - e) * (a / e).ln();
        }
    }
    total
}

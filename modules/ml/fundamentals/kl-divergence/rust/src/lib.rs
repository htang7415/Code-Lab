pub fn kl(p: &[f64], q: &[f64]) -> f64 {
    let mut total = 0.0;
    for (&pi, &qi) in p.iter().zip(q.iter()) {
        if pi > 0.0 && qi > 0.0 {
            total += pi * (pi / qi).ln();
        }
    }
    total
}

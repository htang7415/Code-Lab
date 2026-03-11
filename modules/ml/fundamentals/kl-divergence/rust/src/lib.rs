pub fn kl(p: &[f64], q: &[f64]) -> f64 {
    assert_eq!(p.len(), q.len(), "p and q must have the same length");

    let mut total = 0.0;
    for (&pi, &qi) in p.iter().zip(q.iter()) {
        assert!(pi >= 0.0 && qi >= 0.0, "p and q must be non-negative");
        if pi == 0.0 {
            continue;
        }
        if qi == 0.0 {
            return f64::INFINITY;
        }
        total += pi * (pi / qi).ln();
    }
    total
}

pub fn js(p: &[f64], q: &[f64]) -> f64 {
    let m: Vec<f64> = p.iter().zip(q.iter()).map(|(a, b)| (a + b) / 2.0).collect();
    let kl = |a: &[f64], b: &[f64]| -> f64 {
        let mut total = 0.0;
        for (&ai, &bi) in a.iter().zip(b.iter()) {
            if ai > 0.0 && bi > 0.0 {
                total += ai * (ai / bi).ln();
            }
        }
        total
    };
    0.5 * kl(p, &m) + 0.5 * kl(q, &m)
}

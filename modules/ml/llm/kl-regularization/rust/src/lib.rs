pub fn kl_penalty(p: &[f64], q: &[f64], beta: f64) -> f64 {
    let mut kl = 0.0;
    for (&pi, &qi) in p.iter().zip(q.iter()) {
        if pi > 0.0 && qi > 0.0 {
            kl += pi * (pi / qi).ln();
        }
    }
    beta * kl
}

pub fn elastic_net_penalty(w: &[f64], l1: f64, l2: f64) -> f64 {
    let l1_term: f64 = w.iter().map(|v| v.abs()).sum();
    let l2_term: f64 = w.iter().map(|v| v * v).sum();
    l1 * l1_term + l2 * l2_term
}

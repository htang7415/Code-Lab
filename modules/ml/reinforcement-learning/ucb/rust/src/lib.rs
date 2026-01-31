pub fn ucb_score(q: f64, t: f64, n: f64, c: f64) -> f64 {
    q + c * (t.ln() / n).sqrt()
}

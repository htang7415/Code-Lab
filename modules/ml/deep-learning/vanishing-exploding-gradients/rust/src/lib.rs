pub fn gradient_chain(weights: &[f64], grad: f64) -> f64 {
    let mut out = grad;
    for w in weights {
        out *= w;
    }
    out
}

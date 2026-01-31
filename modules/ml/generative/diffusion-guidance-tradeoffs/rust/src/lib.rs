pub fn guided_step(base: f64, cond: f64, scale: f64) -> f64 {
    base + scale * (cond - base)
}

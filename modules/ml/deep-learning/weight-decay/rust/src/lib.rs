pub fn weight_decay_step(w: f64, grad: f64, lr: f64, lam: f64) -> f64 {
    w - lr * (grad + lam * w)
}

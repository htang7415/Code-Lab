pub fn step(w: f64, grad: f64, lr: f64) -> f64 {
    w - lr * grad
}

pub fn gd_step(x: f64, grad: f64, lr: f64) -> f64 {
    x - lr * grad
}

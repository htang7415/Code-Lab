pub fn adagrad_step(w: f64, grad: f64, g2: f64, lr: f64, eps: f64) -> (f64, f64) {
    let g2_new = g2 + grad * grad;
    let w_new = w - lr * grad / (g2_new.sqrt() + eps);
    (w_new, g2_new)
}

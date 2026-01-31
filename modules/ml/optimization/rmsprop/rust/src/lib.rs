pub fn rmsprop_step(w: f64, grad: f64, v: f64, lr: f64, beta: f64, eps: f64) -> (f64, f64) {
    let v_new = beta * v + (1.0 - beta) * grad * grad;
    let w_new = w - lr * grad / (v_new.sqrt() + eps);
    (w_new, v_new)
}

pub fn nesterov_step(w: f64, grad: f64, v: f64, lr: f64, mu: f64) -> (f64, f64) {
    let v_new = mu * v + grad;
    let w_new = w - lr * (mu * v_new + grad);
    (w_new, v_new)
}

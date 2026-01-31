pub fn adamw_step(w: f64, grad: f64, m: f64, v: f64, lr: f64, wd: f64, beta1: f64, beta2: f64, eps: f64) -> (f64, f64, f64) {
    let m_new = beta1 * m + (1.0 - beta1) * grad;
    let v_new = beta2 * v + (1.0 - beta2) * grad * grad;
    let w_new = w - lr * m_new / (v_new.sqrt() + eps) - lr * wd * w;
    (w_new, m_new, v_new)
}

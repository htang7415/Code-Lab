pub fn dynamic_tanh(x: f64, alpha: f64, gamma: f64, beta: f64) -> f64 {
    gamma * (alpha * x).tanh() + beta
}

pub fn activations(x: f64) -> (f64, f64, f64, f64, f64) {
    let sigmoid = 1.0 / (1.0 + (-x).exp());
    let tanh = x.tanh();
    let hard_sigmoid = (0.2 * x + 0.5).clamp(0.0, 1.0);
    let hardtanh = x.clamp(-1.0, 1.0);
    let dynamic = dynamic_tanh(x, 1.2, 1.0, 0.0);
    (sigmoid, tanh, hard_sigmoid, hardtanh, dynamic)
}

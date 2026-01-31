pub fn modern_activations(x: f64) -> (f64, f64, f64, f64) {
    let sigmoid = 1.0 / (1.0 + (-x).exp());
    let swish = x * sigmoid;
    let gelu = 0.5 * x * (1.0 + ( (2.0 / std::f64::consts::PI).sqrt() * (x + 0.044715 * x.powi(3)) ).tanh());
    let mish = x * (1.0 + x.exp()).ln().tanh();
    let swiglu = (x * sigmoid) * x;
    (swish, gelu, mish, swiglu)
}

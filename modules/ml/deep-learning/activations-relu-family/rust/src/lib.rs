pub fn relu_family(x: f64, alpha: f64) -> (f64, f64, f64, f64) {
    let relu = x.max(0.0);
    let leaky = if x > 0.0 { x } else { alpha * x };
    let elu = if x > 0.0 { x } else { alpha * (x.exp() - 1.0) };
    let prelu = if x > 0.0 { x } else { alpha * x };
    (relu, leaky, elu, prelu)
}

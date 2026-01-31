pub fn propagate_variance(var: f64, layer_vars: &[f64]) -> f64 {
    let mut out = var;
    for v in layer_vars {
        out *= v;
    }
    out
}

pub fn forward(x: &[f64], w: &[f64], b: f64) -> f64 {
    let mut out = b;
    for (wi, xi) in w.iter().zip(x.iter()) {
        out += wi * xi;
    }
    out
}

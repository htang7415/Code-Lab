pub fn bilinear_sample(v00: f64, v01: f64, v10: f64, v11: f64, tx: f64, ty: f64) -> f64 {
    let a = v00 * (1.0 - tx) + v10 * tx;
    let b = v01 * (1.0 - tx) + v11 * tx;
    a * (1.0 - ty) + b * ty
}

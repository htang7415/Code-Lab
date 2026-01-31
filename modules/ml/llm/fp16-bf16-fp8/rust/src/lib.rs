pub fn quantize_fp(x: f64, mantissa_bits: i32) -> f64 {
    if x == 0.0 {
        return 0.0;
    }
    let exp = x.abs().log2().floor() as i32;
    let scale = 2f64.powi(mantissa_bits - exp);
    (x * scale).round() / scale
}

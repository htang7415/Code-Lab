pub fn quantize_int(x: f64, bits: i32, scale: f64) -> i32 {
    let qmax = (1 << (bits - 1)) - 1;
    let q = (x / scale).round() as i32;
    q.max(-qmax).min(qmax)
}

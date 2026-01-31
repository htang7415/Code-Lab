pub fn dropout(x: &[f64], p: f64, seed: u64) -> Vec<f64> {
    let mut out = Vec::with_capacity(x.len());
    let mut state = seed;
    for &v in x {
        state = (1103515245u64.wrapping_mul(state).wrapping_add(12345)) % (1u64 << 31);
        let keep = (state as f64 / ((1u64 << 31) - 1) as f64) > p;
        if keep {
            out.push(v / (1.0 - p));
        } else {
            out.push(0.0);
        }
    }
    out
}

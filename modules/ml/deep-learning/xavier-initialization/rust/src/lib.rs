pub fn xavier_uniform(fan_in: usize, fan_out: usize, seed: u64) -> Vec<f64> {
    let limit = (6.0 / (fan_in + fan_out) as f64).sqrt();
    let mut state = seed;
    let mut out = Vec::with_capacity(fan_in * fan_out);
    for _ in 0..fan_in * fan_out {
        state = (1103515245u64.wrapping_mul(state).wrapping_add(12345)) % (1u64 << 31);
        let frac = state as f64 / ((1u64 << 31) - 1) as f64;
        out.push(-limit + frac * (2.0 * limit));
    }
    out
}

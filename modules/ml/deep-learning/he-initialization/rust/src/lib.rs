pub fn he_normal(fan_in: usize, fan_out: usize, seed: u64) -> Vec<f64> {
    let std = (2.0 / fan_in as f64).sqrt();
    let mut values = Vec::new();
    let mut state = seed;
    while values.len() < fan_in * fan_out {
        state = (1103515245u64.wrapping_mul(state).wrapping_add(12345)) % (1u64 << 31);
        let u1 = (state as f64 / ((1u64 << 31) - 1) as f64).max(1e-6);
        state = (1103515245u64.wrapping_mul(state).wrapping_add(12345)) % (1u64 << 31);
        let u2 = state as f64 / ((1u64 << 31) - 1) as f64;
        let z0 = (-2.0 * u1.ln()).sqrt() * (2.0 * std::f64::consts::PI * u2).cos();
        let z1 = (-2.0 * u1.ln()).sqrt() * (2.0 * std::f64::consts::PI * u2).sin();
        values.push(z0 * std);
        if values.len() < fan_in * fan_out {
            values.push(z1 * std);
        }
    }
    values
}

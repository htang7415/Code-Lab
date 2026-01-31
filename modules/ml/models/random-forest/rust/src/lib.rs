pub fn bootstrap_indices(n: usize, seed: u64) -> Vec<usize> {
    let mut idxs = Vec::with_capacity(n);
    let mut state = seed;
    for _ in 0..n {
        state = (1103515245u64.wrapping_mul(state).wrapping_add(12345)) % (1u64 << 31);
        idxs.push((state as usize) % n);
    }
    idxs
}

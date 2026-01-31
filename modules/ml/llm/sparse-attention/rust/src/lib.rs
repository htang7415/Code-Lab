pub fn window_mask(seq_len: usize, window: usize) -> Vec<Vec<i32>> {
    let mut mask = vec![vec![0; seq_len]; seq_len];
    for i in 0..seq_len {
        for j in 0..seq_len {
            let dist = if i > j { i - j } else { j - i };
            if dist <= window {
                mask[i][j] = 1;
            }
        }
    }
    mask
}

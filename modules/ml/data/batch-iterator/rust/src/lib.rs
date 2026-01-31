pub fn batch_indices(n: usize, batch_size: usize) -> Vec<Vec<usize>> {
    let mut batches = Vec::new();
    let mut start = 0;
    while start < n {
        let end = usize::min(n, start + batch_size);
        batches.push((start..end).collect());
        start += batch_size;
    }
    batches
}

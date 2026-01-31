pub fn batch_requests(n: usize, batch_size: usize) -> usize {
    (n + batch_size - 1) / batch_size
}

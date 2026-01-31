pub fn num_batches(dataset_size: usize, batch_size: usize) -> usize {
    (dataset_size + batch_size - 1) / batch_size
}

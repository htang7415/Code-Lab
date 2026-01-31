pub fn split_indices(n: usize, train_frac: f64, val_frac: f64) -> (Vec<usize>, Vec<usize>, Vec<usize>) {
    let n_train = (n as f64 * train_frac).floor() as usize;
    let n_val = (n as f64 * val_frac).floor() as usize;
    let train: Vec<usize> = (0..n_train).collect();
    let val: Vec<usize> = (n_train..(n_train + n_val)).collect();
    let test: Vec<usize> = (n_train + n_val..n).collect();
    (train, val, test)
}

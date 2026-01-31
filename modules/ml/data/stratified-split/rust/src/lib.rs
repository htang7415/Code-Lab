use std::collections::HashMap;

pub fn stratified_split(labels: &[i32], train_frac: f64) -> (Vec<usize>, Vec<usize>) {
    let mut buckets: HashMap<i32, Vec<usize>> = HashMap::new();
    for (idx, label) in labels.iter().enumerate() {
        buckets.entry(*label).or_default().push(idx);
    }
    let mut train = Vec::new();
    let mut test = Vec::new();
    for idxs in buckets.values() {
        let cut = (idxs.len() as f64 * train_frac) as usize;
        train.extend_from_slice(&idxs[..cut]);
        test.extend_from_slice(&idxs[cut..]);
    }
    (train, test)
}

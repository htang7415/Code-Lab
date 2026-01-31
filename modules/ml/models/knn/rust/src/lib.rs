use std::collections::HashMap;

pub fn knn_predict(distances: &[f64], labels: &[i32], k: usize) -> i32 {
    let mut idxs: Vec<usize> = (0..distances.len()).collect();
    idxs.sort_by(|&a, &b| distances[a].partial_cmp(&distances[b]).unwrap());
    let mut counts: HashMap<i32, usize> = HashMap::new();
    for &i in idxs.iter().take(k) {
        *counts.entry(labels[i]).or_insert(0) += 1;
    }
    counts.into_iter().max_by_key(|(_, c)| *c).unwrap().0
}

use std::collections::HashMap;

pub fn class_weights(labels: &[i32]) -> HashMap<i32, f64> {
    let mut counts: HashMap<i32, usize> = HashMap::new();
    for label in labels {
        *counts.entry(*label).or_insert(0) += 1;
    }
    let n = labels.len() as f64;
    let k = counts.len() as f64;
    let mut weights = HashMap::new();
    for (cls, cnt) in counts {
        weights.insert(cls, n / (k * cnt as f64));
    }
    weights
}

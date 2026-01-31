use std::collections::HashMap;

pub fn gini(labels: &[i32]) -> f64 {
    let mut counts: HashMap<i32, usize> = HashMap::new();
    for label in labels {
        *counts.entry(*label).or_insert(0) += 1;
    }
    let n = labels.len() as f64;
    let mut sum_sq = 0.0;
    for cnt in counts.values() {
        let p = *cnt as f64 / n;
        sum_sq += p * p;
    }
    1.0 - sum_sq
}

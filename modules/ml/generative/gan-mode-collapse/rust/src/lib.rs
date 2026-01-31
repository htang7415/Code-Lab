use std::collections::HashSet;

pub fn diversity_score(samples: &[i32]) -> f64 {
    if samples.is_empty() { return 0.0; }
    let set: HashSet<i32> = samples.iter().copied().collect();
    set.len() as f64 / samples.len() as f64
}

use std::collections::HashSet;

pub fn jaccard(a: &HashSet<i32>, b: &HashSet<i32>) -> f64 {
    let inter = a.intersection(b).count() as f64;
    let union = a.union(b).count() as f64;
    if union == 0.0 { 0.0 } else { inter / union }
}

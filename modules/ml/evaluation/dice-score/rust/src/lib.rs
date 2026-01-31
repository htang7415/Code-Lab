use std::collections::HashSet;

pub fn dice(a: &HashSet<i32>, b: &HashSet<i32>) -> f64 {
    let inter = a.intersection(b).count() as f64;
    let denom = (a.len() + b.len()) as f64;
    if denom == 0.0 { 0.0 } else { 2.0 * inter / denom }
}

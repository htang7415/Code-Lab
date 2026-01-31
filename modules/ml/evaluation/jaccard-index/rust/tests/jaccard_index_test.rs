use ml_evaluation_jaccard_index::jaccard;
use std::collections::HashSet;

#[test]
fn test_jaccard() {
    let a: HashSet<i32> = [1, 2].into_iter().collect();
    let b: HashSet<i32> = [2, 3].into_iter().collect();
    assert!((jaccard(&a, &b) - 1.0 / 3.0).abs() < 1e-6);
}

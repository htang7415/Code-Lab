use ml_evaluation_dice_score::dice;
use std::collections::HashSet;

#[test]
fn test_dice() {
    let a: HashSet<i32> = [1, 2].into_iter().collect();
    let b: HashSet<i32> = [2, 3].into_iter().collect();
    assert!((dice(&a, &b) - 0.5).abs() < 1e-6);
}

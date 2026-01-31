use std::collections::HashSet;

pub fn has_leakage(train_ids: &[i32], test_ids: &[i32]) -> bool {
    let train: HashSet<i32> = train_ids.iter().copied().collect();
    test_ids.iter().any(|id| train.contains(id))
}

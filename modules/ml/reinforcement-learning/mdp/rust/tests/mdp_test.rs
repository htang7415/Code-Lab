use ml_reinforcement_learning_mdp::transition_prob;
use std::collections::HashMap;

#[test]
fn test_transition_prob() {
    let mut map = HashMap::new();
    let mut next = HashMap::new();
    next.insert(2, 0.8);
    map.insert((0, 1), next);
    assert_eq!(transition_prob(&map, 0, 1, 2), 0.8);
}

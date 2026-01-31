use ml_reinforcement_learning_reinforce::reinforce_update;

#[test]
fn test_reinforce_update() {
    assert!((reinforce_update(2.0, 1.0, 0.1) - 0.2).abs() < 1e-6);
}

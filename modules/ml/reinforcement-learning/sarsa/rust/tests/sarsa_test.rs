use ml_reinforcement_learning_sarsa::sarsa_update;

#[test]
fn test_sarsa_update() {
    assert!((sarsa_update(0.0, 1.0, 0.0, 0.5, 0.9) - 0.5).abs() < 1e-6);
}

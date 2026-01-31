use ml_reinforcement_learning_q_learning::q_update;

#[test]
fn test_q_update() {
    assert!((q_update(0.0, 1.0, 0.0, 0.5, 0.9) - 0.5).abs() < 1e-6);
}

use ml_reinforcement_learning_bandits::update_value;

#[test]
fn test_update_value() {
    assert_eq!(update_value(0.0, 1, 1.0), 1.0);
}

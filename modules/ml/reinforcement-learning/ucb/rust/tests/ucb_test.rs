use ml_reinforcement_learning_ucb::ucb_score;

#[test]
fn test_ucb_score() {
    assert!(ucb_score(0.5, 10.0, 2.0, 1.0) > 0.5);
}

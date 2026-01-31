use ml_reinforcement_learning_ppo::clip_ratio;

#[test]
fn test_clip_ratio() {
    assert_eq!(clip_ratio(1.5, 0.2), 1.2);
}

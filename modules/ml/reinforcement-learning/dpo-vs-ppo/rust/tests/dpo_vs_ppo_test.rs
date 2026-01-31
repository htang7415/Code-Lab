use ml_reinforcement_learning_dpo_vs_ppo::compare_methods;

#[test]
fn test_compare_methods() {
    assert!(compare_methods().contains(&"dpo"));
}

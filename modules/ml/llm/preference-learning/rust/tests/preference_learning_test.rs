use ml_llm_preference_learning::preference_loss;

#[test]
fn test_preference_loss() {
    let loss = preference_loss(2.0, 0.5);
    assert!(loss < 0.2);
}

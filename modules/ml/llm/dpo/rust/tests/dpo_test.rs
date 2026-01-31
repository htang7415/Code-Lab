use ml_llm_dpo::dpo_loss;

#[test]
fn test_dpo_loss() {
    let loss = dpo_loss(1.0, 0.2, 0.5);
    assert!(loss < 0.6);
}

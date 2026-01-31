use ml_llm_rlhf::reward_model_loss;

#[test]
fn test_reward_model_loss() {
    let loss = reward_model_loss(1.2, 0.0);
    assert!(loss < 0.4);
}

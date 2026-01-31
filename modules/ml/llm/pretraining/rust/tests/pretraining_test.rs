use ml_llm_pretraining::next_token_loss;

#[test]
fn test_next_token_loss() {
    let logits = vec![vec![2.0, 0.0], vec![0.0, 2.0]];
    let loss = next_token_loss(&logits, &[0, 1]);
    assert!(loss < 0.2);
}

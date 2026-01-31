use ml_llm_supervised_fine_tuning::sft_loss;

#[test]
fn test_sft_loss_mask() {
    let logits = vec![vec![2.0, 0.0], vec![0.0, 2.0]];
    let loss = sft_loss(&logits, &[0, 1], &[1, 0]);
    assert!(loss < 0.2);
}

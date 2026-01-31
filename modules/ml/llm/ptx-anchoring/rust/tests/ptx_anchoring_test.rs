use ml_llm_ptx_anchoring::anchored_loss;

#[test]
fn test_anchored_loss() {
    let loss = anchored_loss(1.0, 0.5, 0.2);
    assert!((loss - 0.9).abs() < 1e-6);
}

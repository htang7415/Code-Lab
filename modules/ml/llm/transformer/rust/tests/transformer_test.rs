use ml_llm_transformer::transformer_block;

#[test]
fn test_transformer_block_shape() {
    let x = vec![vec![0.1, 0.2], vec![0.0, 0.3]];
    let w1 = vec![vec![0.5, 0.0], vec![0.0, 0.5]];
    let w2 = vec![vec![1.0, 0.0], vec![0.0, 1.0]];
    let out = transformer_block(&x, &w1, &w2);
    assert_eq!(out.len(), 2);
    assert_eq!(out[0].len(), 2);
}

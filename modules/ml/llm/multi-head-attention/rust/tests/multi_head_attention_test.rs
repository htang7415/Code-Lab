use ml_llm_multi_head_attention::multi_head_attention;

#[test]
fn test_multi_head_attention_shape() {
    let q = vec![vec![1.0, 0.0, 0.0, 1.0]; 2];
    let out = multi_head_attention(&q, &q, &q, 2);
    assert_eq!(out.len(), 2);
    assert_eq!(out[0].len(), 4);
}

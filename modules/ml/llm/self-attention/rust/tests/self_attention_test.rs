use ml_llm_self_attention::self_attention;

#[test]
fn test_self_attention_shape() {
    let q = vec![vec![1.0, 0.0], vec![0.0, 1.0]];
    let k = q.clone();
    let v = vec![vec![1.0, 2.0], vec![3.0, 4.0]];
    let out = self_attention(&q, &k, &v);
    assert_eq!(out.len(), 2);
    assert_eq!(out[0].len(), 2);
}

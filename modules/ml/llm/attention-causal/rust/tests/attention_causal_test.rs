use ml_llm_attention_causal::{causal_mask, causal_self_attention};

#[test]
fn test_causal_mask() {
    let mask = causal_mask(3);
    assert!(mask[0][1].is_infinite());
    assert_eq!(mask[2][1], 0.0);
}

#[test]
fn test_causal_self_attention_shape() {
    let q = vec![vec![1.0, 0.0], vec![0.0, 1.0]];
    let out = causal_self_attention(&q, &q, &q);
    assert_eq!(out.len(), 2);
    assert_eq!(out[0].len(), 2);
}

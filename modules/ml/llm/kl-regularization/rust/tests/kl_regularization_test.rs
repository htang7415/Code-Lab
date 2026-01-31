use ml_llm_kl_regularization::kl_penalty;

#[test]
fn test_kl_penalty() {
    let p = vec![0.5, 0.5];
    let q = vec![0.9, 0.1];
    let penalty = kl_penalty(&p, &q, 0.1);
    assert!(penalty > 0.0);
}

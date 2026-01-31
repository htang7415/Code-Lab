use ml_llm_moe_routing::moe_combine;

#[test]
fn test_moe_combine() {
    let experts = vec![vec![1.0, 0.0], vec![0.0, 2.0]];
    let out = moe_combine(&experts, &[0.2, 0.8], 1);
    assert_eq!(out, vec![0.0, 2.0]);
}

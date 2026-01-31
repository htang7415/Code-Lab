use ml_llm_qlora::qlora_update;

#[test]
fn test_qlora_update() {
    let w = vec![vec![1.05, 0.0], vec![0.0, 1.0]];
    let a = vec![vec![1.0], vec![0.0]];
    let b = vec![vec![2.0, 0.0]];
    let out = qlora_update(&w, &a, &b, 1.0, 0.1);
    assert!(out[0][0] > 1.0);
}

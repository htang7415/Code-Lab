use ml_llm_lora::lora_update;

#[test]
fn test_lora_update() {
    let w = vec![vec![1.0, 0.0], vec![0.0, 1.0]];
    let a = vec![vec![1.0], vec![0.0]];
    let b = vec![vec![2.0, 0.0]];
    let out = lora_update(&w, &a, &b, 1.0);
    assert!(out[0][0] > 1.0);
}

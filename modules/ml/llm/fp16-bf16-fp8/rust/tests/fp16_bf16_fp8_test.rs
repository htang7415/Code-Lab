use ml_llm_fp16_bf16_fp8::quantize_fp;

#[test]
fn test_quantize_fp() {
    let out = quantize_fp(1.2345, 3);
    assert!((out - 1.25).abs() < 0.1);
}

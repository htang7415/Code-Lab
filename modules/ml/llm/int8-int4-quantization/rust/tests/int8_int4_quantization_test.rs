use ml_llm_int8_int4_quantization::quantize_int;

#[test]
fn test_quantize_int() {
    let q = quantize_int(1.2, 4, 0.1);
    assert!(q <= 7);
}

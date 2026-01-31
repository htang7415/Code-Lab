use ml_llm_positional_encoding::sinusoidal_position;

#[test]
fn test_positional_encoding_shape() {
    let vec = sinusoidal_position(3, 6);
    assert_eq!(vec.len(), 6);
    assert!(vec[0] != vec[1]);
}

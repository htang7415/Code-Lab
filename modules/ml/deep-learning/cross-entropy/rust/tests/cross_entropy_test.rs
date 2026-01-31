use ml_deep_learning_cross_entropy::cross_entropy;

#[test]
fn test_cross_entropy_low() {
    let loss = cross_entropy(&[3.0, 0.0], 0);
    assert!(loss < 0.1);
}

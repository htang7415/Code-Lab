use ml_deep_learning_dropout::dropout;

#[test]
fn test_dropout_length() {
    let out = dropout(&[1.0, 2.0, 3.0], 0.5, 1);
    assert_eq!(out.len(), 3);
}

use ml_deep_learning_groupnorm::groupnorm;

#[test]
fn test_groupnorm_length() {
    let out = groupnorm(&[1.0, 2.0, 3.0, 4.0], 2, 1e-5);
    assert_eq!(out.len(), 4);
}

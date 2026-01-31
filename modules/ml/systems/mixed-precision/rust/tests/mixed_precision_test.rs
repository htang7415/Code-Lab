use ml_systems_mixed_precision::scale_gradients;

#[test]
fn test_scale_gradients() {
    assert_eq!(scale_gradients(&[1.0, 2.0], 2.0), vec![2.0, 4.0]);
}

use ml_systems_forward_pass::forward;

#[test]
fn test_forward() {
    assert_eq!(forward(&[1.0, 2.0], &[1.0, 1.0], 0.0), 3.0);
}

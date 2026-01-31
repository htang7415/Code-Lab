use ml_systems_backward_pass::backward;

#[test]
fn test_backward() {
    assert_eq!(backward(2.0, 3.0), 6.0);
}

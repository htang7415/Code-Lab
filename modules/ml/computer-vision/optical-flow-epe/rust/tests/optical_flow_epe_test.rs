use ml_computer_vision_optical_flow_epe::epe;

#[test]
fn test_epe() {
    assert_eq!(epe((0.0, 0.0), (3.0, 4.0)), 5.0);
}

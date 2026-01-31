use ml_systems_debug_overfit_underfit::diagnose;

#[test]
fn test_diagnose() {
    assert_eq!(diagnose(0.2, 0.5), "overfit");
}

use ml_mlops_offline_online_inference::is_online;

#[test]
fn test_is_online() {
    assert!(is_online(50.0, 100.0));
    assert!(!is_online(500.0, 100.0));
}

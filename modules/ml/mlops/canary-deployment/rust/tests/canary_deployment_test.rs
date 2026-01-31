use ml_mlops_canary_deployment::split_traffic;

#[test]
fn test_split_traffic() {
    assert_eq!(split_traffic(100, 0.1), (10, 90));
}

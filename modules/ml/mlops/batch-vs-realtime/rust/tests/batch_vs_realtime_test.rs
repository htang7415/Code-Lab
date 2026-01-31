use ml_mlops_batch_vs_realtime::choose_mode;

#[test]
fn test_choose_mode() {
    assert_eq!(choose_mode(1), "realtime");
    assert_eq!(choose_mode(8), "batch");
}

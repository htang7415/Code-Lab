use ml_fundamentals_two_sample_t_test::t_stat;

#[test]
fn test_t_stat() {
    assert!(t_stat(&[1.0, 1.0, 1.0], &[2.0, 2.0, 2.0]) < 0.0);
}

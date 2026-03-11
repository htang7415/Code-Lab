use ml_fundamentals_two_sample_t_test::t_stat;

#[test]
fn test_t_stat_sign_matches_mean_difference() {
    assert!(t_stat(&[1.0, 1.0, 1.0], &[2.0, 2.0, 2.0]) < 0.0);
}

#[test]
fn test_t_stat_handles_zero_variance_with_equal_means() {
    assert_eq!(t_stat(&[1.0, 1.0, 1.0], &[1.0, 1.0, 1.0]), 0.0);
}

#[test]
#[should_panic(expected = "each sample must contain at least 2 observations")]
fn test_t_stat_requires_at_least_two_observations_per_group() {
    let _ = t_stat(&[1.0], &[2.0, 3.0]);
}

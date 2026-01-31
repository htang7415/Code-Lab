use ml_mlops_sla_metrics::violation_rate;

#[test]
fn test_violation_rate() {
    assert!((violation_rate(2, 10) - 0.2).abs() < 1e-6);
}

use ml_fundamentals_empirical_pmf::empirical_pmf;

#[test]
fn test_empirical_pmf() {
    let pmf = empirical_pmf(&[1, 1, 2]);
    assert!((pmf[&1] - 2.0 / 3.0).abs() < 1e-6);
}

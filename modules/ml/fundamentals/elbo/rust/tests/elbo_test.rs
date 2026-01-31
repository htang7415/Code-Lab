use ml_fundamentals_elbo::elbo;

#[test]
fn test_elbo() {
    assert_eq!(elbo(2.0, 0.5), 1.5);
}

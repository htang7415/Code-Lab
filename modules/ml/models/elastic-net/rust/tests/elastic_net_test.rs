use ml_models_elastic_net::elastic_net_penalty;

#[test]
fn test_elastic_net_penalty() {
    let val = elastic_net_penalty(&[1.0, -2.0], 0.1, 0.1);
    assert!((val - 0.8).abs() < 1e-6);
}

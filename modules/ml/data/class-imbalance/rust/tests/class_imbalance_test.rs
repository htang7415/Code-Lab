use ml_data_class_imbalance::class_weights;

#[test]
fn test_class_weights() {
    let weights = class_weights(&[0, 0, 1]);
    assert!(weights[&1] > weights[&0]);
}

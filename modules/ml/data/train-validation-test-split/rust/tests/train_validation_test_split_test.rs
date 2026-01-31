use ml_data_train_validation_test_split::split_indices;

#[test]
fn test_split_indices() {
    let (train, val, test) = split_indices(10, 0.6, 0.2);
    assert_eq!(train.len(), 6);
    assert_eq!(val.len(), 2);
    assert_eq!(test.len(), 2);
}

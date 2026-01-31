use ml_data_stratified_split::stratified_split;

#[test]
fn test_stratified_split() {
    let labels = vec![0, 0, 1, 1];
    let (train, test) = stratified_split(&labels, 0.5);
    assert_eq!(train.len(), 2);
    assert_eq!(test.len(), 2);
}

use ml_data_batch_iterator::batch_indices;

#[test]
fn test_batch_indices() {
    let batches = batch_indices(5, 2);
    assert_eq!(batches, vec![vec![0, 1], vec![2, 3], vec![4]]);
}

use ml_data_dataset_batch_epoch::num_batches;

#[test]
fn test_num_batches() {
    assert_eq!(num_batches(10, 4), 3);
}

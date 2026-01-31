use ml_mlops_request_batching::batch_requests;

#[test]
fn test_batch_requests() {
    assert_eq!(batch_requests(9, 4), 3);
}

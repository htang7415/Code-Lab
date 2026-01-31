use ml_llm_sparse_attention::window_mask;

#[test]
fn test_window_mask() {
    let mask = window_mask(4, 1);
    assert_eq!(mask[0], vec![1, 1, 0, 0]);
}

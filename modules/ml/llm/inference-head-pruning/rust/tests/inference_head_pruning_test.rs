use ml_llm_inference_head_pruning::prune_heads;

#[test]
fn test_prune_heads() {
    let weights = vec![vec![1.0, 2.0, 3.0, 4.0]];
    let pruned = prune_heads(&weights, &[1], 2);
    assert_eq!(pruned, vec![vec![3.0, 4.0]]);
}

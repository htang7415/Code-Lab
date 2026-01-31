use ml_llm_embeddings::embed;

#[test]
fn test_embed_lookup() {
    let table = vec![vec![0.0, 0.1], vec![1.0, 1.1], vec![2.0, 2.1]];
    let out = embed(&[2, 0], &table);
    assert_eq!(out, vec![vec![2.0, 2.1], vec![0.0, 0.1]]);
}

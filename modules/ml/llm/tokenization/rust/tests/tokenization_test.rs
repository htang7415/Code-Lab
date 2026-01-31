use ml_llm_tokenization::{build_vocab, tokenize};

#[test]
fn test_tokenize_basic() {
    let vocab = build_vocab(&["hello world", "hello there"]);
    let ids = tokenize("hello world", &vocab);
    assert_eq!(ids, vec![vocab["hello"], vocab["world"]]);
}

use std::collections::HashMap;

pub fn build_vocab(texts: &[&str]) -> HashMap<String, usize> {
    let mut vocab = HashMap::new();
    for text in texts {
        for token in text.to_lowercase().split_whitespace() {
            if !vocab.contains_key(token) {
                let id = vocab.len();
                vocab.insert(token.to_string(), id);
            }
        }
    }
    vocab
}

pub fn tokenize(text: &str, vocab: &HashMap<String, usize>) -> Vec<usize> {
    text.to_lowercase()
        .split_whitespace()
        .filter_map(|tok| vocab.get(tok).copied())
        .collect()
}

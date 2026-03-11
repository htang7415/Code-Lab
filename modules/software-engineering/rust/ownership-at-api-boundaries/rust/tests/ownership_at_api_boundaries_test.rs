use software_engineering_rust_ownership_at_api_boundaries::{rename, take_title, title_len, Document};

#[test]
fn test_borrowing_reads_without_consuming_document() {
    let doc = Document::new("draft", "body");
    assert_eq!(title_len(&doc), 5);
    assert_eq!(doc.body, "body");
}

#[test]
fn test_mutable_borrow_updates_title_in_place() {
    let mut doc = Document::new("draft", "body");
    rename(&mut doc, "final");
    assert_eq!(doc.title, "final");
}

#[test]
fn test_consuming_document_moves_title_out() {
    let doc = Document::new("draft", "body");
    let title = take_title(doc);
    assert_eq!(title, "draft");
}

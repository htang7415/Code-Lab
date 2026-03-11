#[derive(Debug, Clone, PartialEq, Eq)]
pub struct Document {
    pub title: String,
    pub body: String,
}

impl Document {
    pub fn new(title: &str, body: &str) -> Self {
        Self {
            title: title.to_string(),
            body: body.to_string(),
        }
    }
}

pub fn title_len(doc: &Document) -> usize {
    doc.title.len()
}

pub fn rename(doc: &mut Document, new_title: &str) {
    doc.title = new_title.to_string();
}

pub fn take_title(doc: Document) -> String {
    doc.title
}

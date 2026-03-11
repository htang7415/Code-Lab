pub trait Formatter {
    fn format(&self, input: &str) -> String;
}

pub struct UppercaseFormatter;

impl Formatter for UppercaseFormatter {
    fn format(&self, input: &str) -> String {
        input.to_uppercase()
    }
}

pub struct PrefixFormatter {
    prefix: String,
}

impl PrefixFormatter {
    pub fn new(prefix: &str) -> Self {
        Self {
            prefix: prefix.to_string(),
        }
    }
}

impl Formatter for PrefixFormatter {
    fn format(&self, input: &str) -> String {
        format!("{}{}", self.prefix, input)
    }
}

pub fn render<F: Formatter>(formatter: &F, input: &str) -> String {
    formatter.format(input)
}

pub fn render_all(formatters: &[&dyn Formatter], input: &str) -> Vec<String> {
    formatters.iter().map(|formatter| formatter.format(input)).collect()
}

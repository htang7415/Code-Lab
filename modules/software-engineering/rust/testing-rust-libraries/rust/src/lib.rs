pub fn normalize_slug(input: &str) -> String {
    let mut out = String::new();
    let mut last_was_dash = false;

    for ch in input.chars() {
        let lowered = ch.to_ascii_lowercase();
        if lowered.is_ascii_alphanumeric() {
            out.push(lowered);
            last_was_dash = false;
        } else if !last_was_dash && !out.is_empty() {
            out.push('-');
            last_was_dash = true;
        }
    }

    out.trim_matches('-').to_string()
}

pub fn test_scope(has_io: bool, pure_logic: bool) -> &'static str {
    if pure_logic {
        "unit"
    } else if has_io {
        "integration"
    } else {
        "unit"
    }
}

pub fn library_ready_for_unit_tests(hidden_globals: usize, injectable_boundaries: usize) -> bool {
    hidden_globals == 0 && injectable_boundaries >= 1
}

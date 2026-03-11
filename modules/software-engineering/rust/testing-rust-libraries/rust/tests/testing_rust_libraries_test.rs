use software_engineering_rust_testing_rust_libraries::{
    library_ready_for_unit_tests, normalize_slug, test_scope,
};

#[test]
fn test_normalize_slug_creates_stable_ascii_slug() {
    assert_eq!(normalize_slug("Hello, Rust!"), "hello-rust");
    assert_eq!(normalize_slug("  multiple   spaces  "), "multiple-spaces");
}

#[test]
fn test_test_scope_prefers_unit_tests_for_pure_logic() {
    assert_eq!(test_scope(false, true), "unit");
    assert_eq!(test_scope(true, false), "integration");
}

#[test]
fn test_library_ready_for_unit_tests_requires_no_hidden_globals_and_injection_points() {
    assert!(library_ready_for_unit_tests(0, 1));
    assert!(!library_ready_for_unit_tests(1, 1));
    assert!(!library_ready_for_unit_tests(0, 0));
}

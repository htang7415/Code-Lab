use software_engineering_rust_traits_and_abstraction_boundaries::{
    render, render_all, Formatter, PrefixFormatter, UppercaseFormatter,
};

#[test]
fn test_render_uses_generic_trait_boundary() {
    let formatter = UppercaseFormatter;
    assert_eq!(render(&formatter, "hi"), "HI");
}

#[test]
fn test_render_all_supports_multiple_trait_object_implementations() {
    let upper = UppercaseFormatter;
    let prefixed = PrefixFormatter::new("id:");
    let formatters: [&dyn Formatter; 2] = [&upper, &prefixed];
    assert_eq!(render_all(&formatters, "42"), vec![String::from("42").to_uppercase(), String::from("id:42")]);
}

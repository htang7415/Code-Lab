use ml_generative_model_selection::choose_model;

#[test]
fn test_choose_model() {
    assert_eq!(choose_model("speed"), "gan");
}

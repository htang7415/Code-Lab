pub fn choose_model(priority: &str) -> String {
    match priority.to_lowercase().as_str() {
        "speed" => "gan".to_string(),
        "diversity" => "diffusion".to_string(),
        _ => "vae".to_string(),
    }
}

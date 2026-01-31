pub fn choose_mode(batch_size: usize) -> String {
    if batch_size > 1 { "batch".to_string() } else { "realtime".to_string() }
}

pub fn rgb_to_gray(r: i32, g: i32, b: i32) -> f64 {
    0.299 * r as f64 + 0.587 * g as f64 + 0.114 * b as f64
}

pub fn normalize_pixels(pixels: &[i32]) -> Vec<f64> {
    pixels.iter().map(|p| *p as f64 / 255.0).collect()
}

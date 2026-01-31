pub fn calinski_harabasz(b: f64, w: f64, k: i32, n: i32) -> f64 {
    (b / (k as f64 - 1.0)) / (w / (n as f64 - k as f64))
}

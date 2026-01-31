pub fn newton_step(x: f64, f_prime: f64, f_double_prime: f64) -> f64 {
    x - f_prime / f_double_prime
}

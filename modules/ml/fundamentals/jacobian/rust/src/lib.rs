pub fn jacobian(f1: fn(f64, f64) -> f64, f2: fn(f64, f64) -> f64, x: f64, y: f64, eps: f64) -> [[f64; 2]; 2] {
    let df1_dx = (f1(x + eps, y) - f1(x - eps, y)) / (2.0 * eps);
    let df1_dy = (f1(x, y + eps) - f1(x, y - eps)) / (2.0 * eps);
    let df2_dx = (f2(x + eps, y) - f2(x - eps, y)) / (2.0 * eps);
    let df2_dy = (f2(x, y + eps) - f2(x, y - eps)) / (2.0 * eps);
    [[df1_dx, df1_dy], [df2_dx, df2_dy]]
}

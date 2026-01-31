pub fn epe(pred: (f64, f64), target: (f64, f64)) -> f64 {
    let dx = pred.0 - target.0;
    let dy = pred.1 - target.1;
    (dx * dx + dy * dy).sqrt()
}

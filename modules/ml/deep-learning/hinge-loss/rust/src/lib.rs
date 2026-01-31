pub fn hinge_loss(score: f64, label: i32) -> f64 {
    let val = 1.0 - (label as f64) * score;
    if val > 0.0 { val } else { 0.0 }
}

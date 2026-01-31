pub fn f1_score(precision: f64, recall: f64) -> f64 {
    if precision + recall == 0.0 { 0.0 } else { 2.0 * precision * recall / (precision + recall) }
}

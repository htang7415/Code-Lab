pub fn precision_recall(y_true: &[i32], y_pred: &[i32]) -> (f64, f64) {
    let mut tp = 0;
    let mut fp = 0;
    let mut fn_ = 0;
    for (t, p) in y_true.iter().zip(y_pred.iter()) {
        if *t == 1 && *p == 1 { tp += 1; }
        if *t == 0 && *p == 1 { fp += 1; }
        if *t == 1 && *p == 0 { fn_ += 1; }
    }
    let precision = if tp + fp > 0 { tp as f64 / (tp + fp) as f64 } else { 0.0 };
    let recall = if tp + fn_ > 0 { tp as f64 / (tp + fn_) as f64 } else { 0.0 };
    (precision, recall)
}

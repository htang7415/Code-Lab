pub fn accuracy(y_true: &[i32], y_pred: &[i32]) -> f64 {
    let mut correct = 0;
    for (a, b) in y_true.iter().zip(y_pred.iter()) {
        if a == b { correct += 1; }
    }
    correct as f64 / y_true.len() as f64
}

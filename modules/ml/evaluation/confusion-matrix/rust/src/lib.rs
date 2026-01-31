pub fn confusion_matrix(y_true: &[i32], y_pred: &[i32]) -> [[i32; 2]; 2] {
    let mut tn = 0;
    let mut fp = 0;
    let mut fn_ = 0;
    let mut tp = 0;
    for (t, p) in y_true.iter().zip(y_pred.iter()) {
        if *t == 0 && *p == 0 { tn += 1; }
        if *t == 0 && *p == 1 { fp += 1; }
        if *t == 1 && *p == 0 { fn_ += 1; }
        if *t == 1 && *p == 1 { tp += 1; }
    }
    [[tn, fp], [fn_, tp]]
}

pub fn auc(fpr: &[f64], tpr: &[f64]) -> f64 {
    let mut area = 0.0;
    for i in 1..fpr.len() {
        area += (fpr[i] - fpr[i - 1]) * (tpr[i] + tpr[i - 1]) / 2.0;
    }
    area
}

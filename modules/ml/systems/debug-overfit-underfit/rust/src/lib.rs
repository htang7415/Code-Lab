pub fn diagnose(train_loss: f64, val_loss: f64) -> String {
    if train_loss < val_loss * 0.7 {
        "overfit".to_string()
    } else if train_loss > 1.0 && val_loss > 1.0 {
        "underfit".to_string()
    } else {
        "ok".to_string()
    }
}

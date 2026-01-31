def diagnose(train_loss: float, val_loss: float) -> str:
    if train_loss < val_loss * 0.7:
        return "overfit"
    if train_loss > 1.0 and val_loss > 1.0:
        return "underfit"
    return "ok"

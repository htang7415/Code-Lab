def anchored_loss(align_loss: float, ptx_loss: float, alpha: float) -> float:
    return (1 - alpha) * align_loss + alpha * ptx_loss

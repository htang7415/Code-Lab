def choose_mode(batch_size: int) -> str:
    return "batch" if batch_size > 1 else "realtime"

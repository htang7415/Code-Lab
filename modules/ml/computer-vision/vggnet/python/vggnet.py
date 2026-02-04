def layers() -> list[str]:
    return [
        "conv3x3",
        "relu",
        "conv3x3",
        "relu",
        "max-pool",
        "conv3x3",
        "relu",
        "conv3x3",
        "relu",
        "max-pool",
        "fc",
        "fc",
        "fc",
    ]

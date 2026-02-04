def layers() -> list[str]:
    return [
        "conv5x5",
        "tanh",
        "avg-pool",
        "conv5x5",
        "tanh",
        "avg-pool",
        "fc",
        "tanh",
        "fc",
        "tanh",
        "fc",
    ]

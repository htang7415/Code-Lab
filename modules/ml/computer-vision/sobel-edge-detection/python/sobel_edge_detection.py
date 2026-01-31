def sobel_center(patch: list[list[float]]) -> float:
    gx = (
        -1 * patch[0][0] + 0 * patch[0][1] + 1 * patch[0][2]
        -2 * patch[1][0] + 0 * patch[1][1] + 2 * patch[1][2]
        -1 * patch[2][0] + 0 * patch[2][1] + 1 * patch[2][2]
    )
    gy = (
        -1 * patch[0][0] -2 * patch[0][1] -1 * patch[0][2]
         0 * patch[1][0] +0 * patch[1][1] +0 * patch[1][2]
         1 * patch[2][0] +2 * patch[2][1] +1 * patch[2][2]
    )
    return (gx ** 2 + gy ** 2) ** 0.5

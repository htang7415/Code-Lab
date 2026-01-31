def conv2d(image: list[list[float]], kernel: list[list[float]]) -> list[list[float]]:
    h = len(image)
    w = len(image[0])
    kh = len(kernel)
    kw = len(kernel[0])
    out = []
    for i in range(h - kh + 1):
        row = []
        for j in range(w - kw + 1):
            val = 0.0
            for u in range(kh):
                for v in range(kw):
                    val += image[i + u][j + v] * kernel[u][v]
            row.append(val)
        out.append(row)
    return out

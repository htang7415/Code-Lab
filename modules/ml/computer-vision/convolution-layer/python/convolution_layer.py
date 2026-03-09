def conv2d(image: list[list[float]], kernel: list[list[float]]) -> list[list[float]]:
    if not image or not image[0]:
        raise ValueError("image must be non-empty")
    if not kernel or not kernel[0]:
        raise ValueError("kernel must be non-empty")
    if any(len(row) != len(image[0]) for row in image):
        raise ValueError("image must be rectangular")
    if any(len(row) != len(kernel[0]) for row in kernel):
        raise ValueError("kernel must be rectangular")

    h = len(image)
    w = len(image[0])
    kh = len(kernel)
    kw = len(kernel[0])
    if kh > h or kw > w:
        raise ValueError("kernel must fit inside the image")

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

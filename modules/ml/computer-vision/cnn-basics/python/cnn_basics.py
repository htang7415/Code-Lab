def conv1d(signal: list[float], kernel: list[float]) -> list[float]:
    out = []
    k = len(kernel)
    for i in range(len(signal) - k + 1):
        out.append(sum(signal[i + j] * kernel[j] for j in range(k)))
    return out

def window_mask(seq_len: int, window: int) -> list[list[int]]:
    mask = [[0 for _ in range(seq_len)] for _ in range(seq_len)]
    for i in range(seq_len):
        for j in range(seq_len):
            if abs(i - j) <= window:
                mask[i][j] = 1
    return mask

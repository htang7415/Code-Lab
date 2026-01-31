def normalize_pixels(pixels: list[int]) -> list[float]:
    return [p / 255.0 for p in pixels]

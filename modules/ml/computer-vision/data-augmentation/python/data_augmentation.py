def horizontal_flip(image: list[list[int]]) -> list[list[int]]:
    return [list(reversed(row)) for row in image]

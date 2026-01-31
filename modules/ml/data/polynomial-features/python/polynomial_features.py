def poly_features(x: float, degree: int) -> list[float]:
    return [x ** d for d in range(1, degree + 1)]

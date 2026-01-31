def assign(points: list[list[float]], centroids: list[list[float]]) -> list[int]:
    assignments = []
    for p in points:
        dists = [sum((pi - ci) ** 2 for pi, ci in zip(p, c)) for c in centroids]
        assignments.append(min(range(len(dists)), key=lambda i: dists[i]))
    return assignments

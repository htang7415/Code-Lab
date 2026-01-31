def davies_bouldin(si: float, sj: float, dij: float) -> float:
    return (si + sj) / dij if dij > 0 else 0.0

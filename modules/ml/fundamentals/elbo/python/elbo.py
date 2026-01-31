def elbo(recon: float, kl: float) -> float:
    return recon - kl

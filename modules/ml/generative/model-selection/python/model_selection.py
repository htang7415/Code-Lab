def choose_model(priority: str) -> str:
    priority = priority.lower()
    if priority == "speed":
        return "gan"
    if priority == "diversity":
        return "diffusion"
    return "vae"

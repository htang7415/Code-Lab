def _validate_rope_pair(pair_index: int, d_model: int, base: float) -> None:
    if d_model <= 0 or d_model % 2 != 0:
        raise ValueError("d_model must be a positive even integer")
    if pair_index < 0 or pair_index >= d_model // 2:
        raise ValueError("pair_index must fit inside the RoPE feature pairs")
    if base <= 1.0:
        raise ValueError("base must be greater than 1")


def rope_pair_frequency(pair_index: int, d_model: int, base: float = 10000.0) -> float:
    _validate_rope_pair(pair_index=pair_index, d_model=d_model, base=base)
    return base ** (-2.0 * pair_index / d_model)


def rope_rotation_angle(
    position: float,
    pair_index: int,
    d_model: int,
    base: float = 10000.0,
) -> float:
    if position < 0:
        raise ValueError("position must be non-negative")
    frequency = rope_pair_frequency(pair_index=pair_index, d_model=d_model, base=base)
    return position * frequency


def linear_scaled_position(position: int, original_context: int, target_context: int) -> float:
    if position < 0:
        raise ValueError("position must be non-negative")
    if original_context <= 0 or target_context <= 0:
        raise ValueError("context lengths must be positive")
    if target_context < original_context:
        raise ValueError("target_context must be at least original_context")
    return position * original_context / target_context


def rope_scaled_angle(
    position: int,
    pair_index: int,
    d_model: int,
    original_context: int,
    target_context: int,
    base: float = 10000.0,
) -> float:
    scaled_position = linear_scaled_position(
        position=position,
        original_context=original_context,
        target_context=target_context,
    )
    return rope_rotation_angle(
        position=scaled_position,
        pair_index=pair_index,
        d_model=d_model,
        base=base,
    )

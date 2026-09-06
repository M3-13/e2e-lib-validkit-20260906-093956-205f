from __future__ import annotations


def clamp(value: int | float, low: int | float, high: int | float) -> int | float:
    for name, arg in (("value", value), ("low", low), ("high", high)):
        if isinstance(arg, bool) or not isinstance(arg, (int, float)):
            raise ValueError(f"{name} must be an int or float")
    if low > high:
        raise ValueError("low must be less than or equal to high")
    return max(low, min(value, high))

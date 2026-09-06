from __future__ import annotations


def mask_secret(text: str, keep: int = 4) -> str:
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    if not isinstance(keep, int) or isinstance(keep, bool):
        raise ValueError("keep must be an integer")
    if keep < 0:
        raise ValueError("keep must not be negative")

    visible = text[-keep:] if keep > 0 else ""
    return "*" * (len(text) - len(visible)) + visible

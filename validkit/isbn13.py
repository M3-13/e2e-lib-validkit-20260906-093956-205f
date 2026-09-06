from __future__ import annotations

import re

_SEPARATORS = re.compile(r"[ -]")


def is_valid_isbn13(text: str) -> bool:
    if not isinstance(text, str):
        raise ValueError("is_valid_isbn13 expects a string")

    digits = _SEPARATORS.sub("", text)
    if len(digits) != 13 or not digits.isdigit():
        return False

    total = sum(
        int(digit) * (1 if index % 2 == 0 else 3) for index, digit in enumerate(digits[:12])
    )
    check_digit = (10 - (total % 10)) % 10
    return check_digit == int(digits[12])

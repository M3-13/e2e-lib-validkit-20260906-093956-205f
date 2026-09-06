from __future__ import annotations


def luhn_check(digits: str | int) -> bool:
    if not isinstance(digits, (str, int)) or isinstance(digits, bool):
        raise ValueError("expected a string or integer of digits")

    value = str(digits)

    if not value.isascii() or not value.isdigit():
        raise ValueError("expected a string or integer of digits")

    total = 0
    double = False
    for char in reversed(value):
        digit = int(char)
        if double:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
        double = not double

    return total % 10 == 0

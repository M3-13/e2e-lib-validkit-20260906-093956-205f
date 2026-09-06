def is_valid_iban(text: str) -> bool:
    if not isinstance(text, str):
        raise ValueError("expected a string")

    compact = text.replace(" ", "")

    if not 15 <= len(compact) <= 34:
        return False

    if not compact[:2].isalpha() or not compact[:2].isascii():
        return False
    if not compact[2:4].isdigit():
        return False

    rearranged = compact[4:] + compact[:4]

    remainder = 0
    for ch in rearranged:
        if "0" <= ch <= "9":
            remainder = (remainder * 10 + ord(ch) - ord("0")) % 97
        elif "A" <= ch.upper() <= "Z":
            value = ord(ch.upper()) - ord("A") + 10
            remainder = (remainder * 100 + value) % 97
        else:
            return False

    return remainder == 1

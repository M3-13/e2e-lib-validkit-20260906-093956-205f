import re

_COUNTRY_CODES = {
    "DE": "49",
    "AT": "43",
    "CH": "41",
}


def normalize_phone(text: str, country_code: str) -> str:
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    if not isinstance(country_code, str):
        raise ValueError("country_code must be a string")

    cc = _resolve_country_code(country_code)

    stripped = text.strip()
    digits = re.sub(r"[^0-9]", "", stripped)
    if not digits:
        raise ValueError("phone number must contain at least one digit")

    if stripped.startswith("+"):
        return "+" + digits

    if digits.startswith("00"):
        return "+" + digits[2:]

    if digits.startswith(cc):
        national = digits[len(cc) :]
    elif digits.startswith("0"):
        national = digits[1:]
    else:
        national = digits

    if not national:
        raise ValueError("phone number has no digits after the country code")

    return "+" + cc + national


def _resolve_country_code(country_code: str) -> str:
    code = country_code.strip().upper()
    if code in _COUNTRY_CODES:
        return _COUNTRY_CODES[code]
    if re.fullmatch(r"[0-9]+", code):
        return code
    raise ValueError("country_code must be an ISO 3166-1 alpha-2 code or a numeric dialing code")

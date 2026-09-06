import unicodedata


def strip_accents(text: str) -> str:
    if not isinstance(text, str):
        raise ValueError("expected str")
    return "".join(c for c in unicodedata.normalize("NFD", text) if not unicodedata.combining(c))

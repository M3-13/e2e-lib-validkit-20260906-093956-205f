import unicodedata


def slugify(text: str) -> str:
    if not isinstance(text, str):
        raise ValueError("slugify expects a string")

    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = "".join(c for c in normalized if not unicodedata.combining(c))
    lowered = ascii_text.lower()
    hyphenated = "".join(c if c.isalnum() else "-" for c in lowered)
    return "-".join(part for part in hyphenated.split("-") if part)

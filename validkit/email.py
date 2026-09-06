import re

_EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")


def is_valid_email(text: str) -> bool:
    if not isinstance(text, str):
        raise ValueError("text must be a str")
    return _EMAIL_RE.fullmatch(text) is not None

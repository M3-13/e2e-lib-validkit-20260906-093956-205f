import pytest

from validkit import strip_accents


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Müller", "Muller"),
        ("Ä", "A"),
        ("Ö", "O"),
        ("Ü", "U"),
        ("Großstraße", "Großstraße"),
        ("café", "cafe"),
        ("naïve", "naive"),
        ("résumé", "resume"),
        ("Zażółć gęślą jaźń", "Zazołc gesla jazn"),
        ("Crème brûlée", "Creme brulee"),
        ("plain text", "plain text"),
        ("", ""),
        ("1234567890", "1234567890"),
    ],
)
def test_strip_accents_removes_diacritics(text: str, expected: str) -> None:
    assert strip_accents(text) == expected


def test_strip_accents_keeps_text_without_accents_unchanged() -> None:
    assert strip_accents("hello world") == "hello world"


@pytest.mark.parametrize("bad", [None, 42, 3.14, ["Müller"], b"M\xc3\xbcller"])
def test_strip_accents_raises_value_error_on_non_str(bad) -> None:
    with pytest.raises(ValueError):
        strip_accents(bad)


def test_strip_accents_error_message_names_only_expected_type() -> None:
    with pytest.raises(ValueError) as excinfo:
        strip_accents(None)
    assert str(excinfo.value) == "expected str"

import pytest

from validkit import is_valid_isbn13


def test_valid_isbn13_plain_digits():
    assert is_valid_isbn13("9780306406157") is True


def test_valid_isbn13_with_hyphens():
    assert is_valid_isbn13("978-0-306-40615-7") is True


def test_valid_isbn13_with_spaces():
    assert is_valid_isbn13("978 0 306 40615 7") is True


def test_valid_isbn13_mixed_separators():
    assert is_valid_isbn13("978-0 306 40615-7") is True


def test_wrong_check_digit_returns_false():
    assert is_valid_isbn13("978-0-306-40615-8") is False


def test_wrong_check_digit_plain_returns_false():
    assert is_valid_isbn13("9780306406158") is False


def test_too_short_returns_false():
    assert is_valid_isbn13("978-0-306-40615") is False


def test_too_long_returns_false():
    assert is_valid_isbn13("978-0-306-40615-77") is False


def test_letters_return_false():
    assert is_valid_isbn13("978-0-306-40615-X") is False


def test_empty_string_returns_false():
    assert is_valid_isbn13("") is False


def test_none_raises_value_error():
    with pytest.raises(ValueError):
        is_valid_isbn13(None)


def test_non_string_raises_value_error():
    with pytest.raises(ValueError):
        is_valid_isbn13(9780306406157)


def test_error_message_names_expected_type_only():
    with pytest.raises(ValueError) as exc_info:
        is_valid_isbn13(None)
    assert "string" in str(exc_info.value)

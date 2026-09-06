import pytest

from validkit import is_valid_iban


def test_valid_iban_without_spaces():
    assert is_valid_iban("DE89370400440532013000") is True


def test_valid_iban_grouped_with_spaces():
    assert is_valid_iban("DE89 3704 0044 0532 0130 00") is True


def test_valid_iban_lowercase():
    assert is_valid_iban("de89 3704 0044 0532 0130 00") is True


def test_tampered_iban_is_false():
    assert is_valid_iban("DE89 3704 0044 0532 0130 01") is False


def test_syntactically_invalid_characters_are_false():
    assert is_valid_iban("DE89!3704 0044 0532 0130 00") is False
    assert is_valid_iban("DE89 3704 0044 0532 0130 00-") is False


def test_too_short_input_is_false():
    assert is_valid_iban("DE89") is False


def test_empty_input_is_false():
    assert is_valid_iban("") is False


def test_non_string_raises_value_error():
    with pytest.raises(ValueError):
        is_valid_iban(None)  # type: ignore[arg-type]
    with pytest.raises(ValueError):
        is_valid_iban(12345)  # type: ignore[arg-type]


def test_value_error_message_does_not_contain_input_value():
    with pytest.raises(ValueError) as excinfo:
        is_valid_iban(12345)  # type: ignore[arg-type]
    assert "12345" not in str(excinfo.value)

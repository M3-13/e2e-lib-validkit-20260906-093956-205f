import pytest

from validkit import normalize_phone


def test_alpha2_country_code_with_trunk_zero():
    assert normalize_phone("0170 1234567", "DE") == "+491701234567"


def test_numeric_country_code():
    assert normalize_phone("0170 1234567", "49") == "+491701234567"


def test_lowercase_alpha2_is_case_insensitive():
    assert normalize_phone("030 1234567", "de") == "+49301234567"


def test_already_international_with_plus():
    assert normalize_phone("+49 170 1234567", "DE") == "+491701234567"


def test_already_international_without_plus():
    assert normalize_phone("491701234567", "DE") == "+491701234567"


def test_international_prefix_00():
    assert normalize_phone("0049 170 1234567", "DE") == "+491701234567"


def test_non_digit_characters_removed():
    assert normalize_phone("(0170) 123-4567", "DE") == "+491701234567"


def test_other_alpha2_country_code():
    assert normalize_phone("0664 123456", "AT") == "+43664123456"


def test_landline_number():
    assert normalize_phone("030 1234567", "DE") == "+49301234567"


def test_non_string_text_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone(None, "DE")
    with pytest.raises(ValueError):
        normalize_phone(12345, "DE")


def test_non_string_country_code_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("0170 1234567", None)
    with pytest.raises(ValueError):
        normalize_phone("0170 1234567", 49)


def test_unknown_country_code_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("0170 1234567", "ZZ")


def test_empty_text_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("", "DE")


def test_text_without_digits_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("+++", "DE")


def test_only_trunk_zero_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("0", "DE")


def test_error_messages_do_not_contain_input_value():
    with pytest.raises(ValueError) as exc:
        normalize_phone("0170 1234567", "ZZ")
    assert "ZZ" not in str(exc.value)
    assert "0170" not in str(exc.value)

    with pytest.raises(ValueError) as exc:
        normalize_phone("", "DE")
    assert "0" not in str(exc.value)

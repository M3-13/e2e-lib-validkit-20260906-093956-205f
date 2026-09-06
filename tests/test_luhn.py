import pytest

from validkit.luhn import luhn_check

VALID_CARD = 4111111111111111


def test_valid_card_as_int_is_true():
    assert luhn_check(VALID_CARD) is True


def test_valid_card_as_str_is_true():
    assert luhn_check("4111111111111111") is True


def test_changed_check_digit_is_false():
    assert luhn_check("4111111111111110") is False


def test_changed_inner_digit_is_false():
    assert luhn_check("4111111211111111") is False


def test_empty_string_raises_value_error():
    with pytest.raises(ValueError):
        luhn_check("")


def test_non_digit_string_raises_value_error():
    with pytest.raises(ValueError):
        luhn_check("abc")


def test_spaces_are_not_accepted():
    with pytest.raises(ValueError):
        luhn_check("4111 1111 1111 1111")


def test_none_raises_value_error():
    with pytest.raises(ValueError):
        luhn_check(None)


def test_float_raises_value_error():
    with pytest.raises(ValueError):
        luhn_check(4111111111111111.0)


def test_bool_raises_value_error():
    with pytest.raises(ValueError):
        luhn_check(True)


def test_negative_int_raises_value_error():
    with pytest.raises(ValueError):
        luhn_check(-4111111111111111)


def test_error_message_does_not_leak_input():
    for bad in ["abc", None, 3.14, ""]:
        with pytest.raises(ValueError) as exc_info:
            luhn_check(bad)
        message = str(exc_info.value)
        assert "abc" not in message
        assert "None" not in message
        assert "3.14" not in message

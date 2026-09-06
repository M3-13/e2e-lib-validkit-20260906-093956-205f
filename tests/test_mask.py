import pytest

from validkit.mask import mask_secret


def test_mask_secret_default_keep():
    assert mask_secret("12345678") == "****5678"


def test_mask_secret_custom_keep():
    assert mask_secret("12345678", 2) == "******78"


def test_mask_secret_keep_zero_masks_everything():
    assert mask_secret("12345678", 0) == "********"


def test_mask_secret_short_text_all_visible():
    assert mask_secret("abc") == "abc"


def test_mask_secret_short_text_partially_masked():
    assert mask_secret("abc", 2) == "*bc"


def test_mask_secret_keep_longer_than_text():
    assert mask_secret("abc", 5) == "abc"


def test_mask_secret_empty_text():
    assert mask_secret("") == ""


def test_mask_secret_negative_keep_raises_value_error():
    with pytest.raises(ValueError):
        mask_secret("12345678", -1)


def test_mask_secret_non_string_text_raises_value_error():
    with pytest.raises(ValueError):
        mask_secret(None)


def test_mask_secret_numeric_text_raises_value_error():
    with pytest.raises(ValueError):
        mask_secret(123)


def test_mask_secret_non_integer_keep_raises_value_error():
    with pytest.raises(ValueError):
        mask_secret("12345678", "4")


def test_mask_secret_error_message_does_not_leak_input():
    with pytest.raises(ValueError) as exc_info:
        mask_secret("secretvalue", -1)
    assert "secretvalue" not in str(exc_info.value)

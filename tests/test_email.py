import time

import pytest

from validkit.email import is_valid_email


@pytest.mark.parametrize(
    "address",
    [
        "test@example.com",
        "user.name@example.com",
        "user+tag@example.co.uk",
        "a@b.co",
        "first.last@sub.example.org",
    ],
)
def test_valid_emails_return_true(address):
    assert is_valid_email(address) is True


@pytest.mark.parametrize(
    "address",
    [
        "a@b",
        "plainaddress",
        "user@example",
        "@example.com",
        "user@.com",
        "user@example.",
        "user name@example.com",
        "user@@example.com",
        "",
    ],
)
def test_invalid_emails_return_false(address):
    assert is_valid_email(address) is False


@pytest.mark.parametrize(
    "value",
    [None, 123, 1.5, ["test@example.com"], {"address": "test@example.com"}, b"test@example.com"],
)
def test_non_str_raises_value_error(value):
    with pytest.raises(ValueError):
        is_valid_email(value)


@pytest.mark.parametrize("value", [None, 123, b"test@example.com"])
def test_value_error_message_names_only_the_expected_type(value):
    with pytest.raises(ValueError, match="str"):
        is_valid_email(value)


def test_ten_thousand_char_input_answered_under_one_second():
    pathological = "a" * 10_000 + "@" + "b" * 10_000
    start = time.perf_counter()
    result = is_valid_email(pathological)
    elapsed = time.perf_counter() - start
    assert result is False
    assert elapsed < 1.0

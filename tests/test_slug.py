import pytest

from validkit.slug import slugify


def test_slugify_removes_accents():
    assert slugify("Héllo, Wörld!") == "hello-world"


def test_slugify_handles_special_characters():
    assert slugify("Hello, World!") == "hello-world"
    assert slugify("foo@bar#baz") == "foo-bar-baz"


def test_slugify_lowercases():
    assert slugify("HelloWORLD") == "helloworld"


def test_slugify_collapses_multiple_hyphens():
    assert slugify("foo---bar") == "foo-bar"
    assert slugify("a  b") == "a-b"


def test_slugify_strips_leading_and_trailing_hyphens():
    assert slugify("-foo-") == "foo"
    assert slugify("   hello   ") == "hello"


def test_slugify_keeps_alphanumeric():
    assert slugify("abc123") == "abc123"


def test_slugify_empty_string():
    assert slugify("") == ""


def test_slugify_rejects_non_string():
    with pytest.raises(ValueError):
        slugify(None)
    with pytest.raises(ValueError):
        slugify(42)
    with pytest.raises(ValueError):
        slugify(["hello"])


def test_slugify_error_message_names_only_expected_type():
    with pytest.raises(ValueError, match="string"):
        slugify(123)
    with pytest.raises(ValueError, match="string"):
        slugify(None)

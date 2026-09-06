import inspect

import validkit

EXPECTED_PARAMS = {
    "is_valid_email": ["text"],
    "luhn_check": ["digits"],
    "is_valid_iban": ["text"],
    "is_valid_isbn13": ["text"],
    "normalize_phone": ["text", "country_code"],
    "strip_accents": ["text"],
    "mask_secret": ["text", "keep"],
    "slugify": ["text"],
    "clamp": ["value", "low", "high"],
}


def test_package_exports_exactly_nine_functions():
    assert set(validkit.__all__) == set(EXPECTED_PARAMS)


def test_every_function_is_available_on_the_package():
    for name in EXPECTED_PARAMS:
        assert callable(getattr(validkit, name))


def test_every_function_has_the_agreed_signature():
    for name, params in EXPECTED_PARAMS.items():
        func = getattr(validkit, name)
        assert list(inspect.signature(func).parameters) == params


def test_mask_secret_keep_default_is_four():
    keep = inspect.signature(validkit.mask_secret).parameters["keep"]
    assert keep.default == 4

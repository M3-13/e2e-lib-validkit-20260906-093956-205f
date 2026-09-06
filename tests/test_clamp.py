import pytest

from validkit import clamp


def test_value_within_range_is_unchanged():
    assert clamp(5, 0, 10) == 5


def test_value_above_range_is_clamped_to_high():
    assert clamp(15, 0, 10) == 10


def test_value_below_range_is_clamped_to_low():
    assert clamp(-5, 0, 10) == 0


def test_value_at_lower_boundary_is_kept():
    assert clamp(0, 0, 10) == 0


def test_value_at_upper_boundary_is_kept():
    assert clamp(10, 0, 10) == 10


def test_float_value_within_range_is_unchanged():
    assert clamp(5.5, 0, 10) == 5.5


def test_float_value_above_range_is_clamped():
    assert clamp(12.3, 0.0, 10.0) == 10.0


def test_float_value_below_range_is_clamped():
    assert clamp(-1.5, 0.0, 10.0) == 0.0


def test_equal_bounds_force_the_bound():
    assert clamp(5, 10, 10) == 10


def test_negative_range_clamps_correctly():
    assert clamp(-3, -10, -1) == -3
    assert clamp(-20, -10, -1) == -10
    assert clamp(0, -10, -1) == -1


def test_low_greater_than_high_raises_value_error():
    with pytest.raises(ValueError):
        clamp(5, 10, 0)


def test_invalid_value_type_raises_value_error():
    with pytest.raises(ValueError):
        clamp(None, 0, 10)
    with pytest.raises(ValueError):
        clamp("5", 0, 10)
    with pytest.raises(ValueError):
        clamp(True, 0, 10)


def test_invalid_bound_type_raises_value_error():
    with pytest.raises(ValueError):
        clamp(5, None, 10)
    with pytest.raises(ValueError):
        clamp(5, 0, "10")


def test_error_message_does_not_contain_input_value():
    with pytest.raises(ValueError) as exc_info:
        clamp("secret-value", 0, 10)
    assert "secret-value" not in str(exc_info.value)

    with pytest.raises(ValueError) as exc_info:
        clamp(5, 10, 0)
    message = str(exc_info.value)
    assert "5" not in message and "10" not in message and "0" not in message

import pytest
from calculator import divide, is_even


def test_divide_basic():
    assert divide(10, 2) == 5


def test_divide_float_result():
    assert divide(7, 2) == 3.5


def test_divide_by_zero_raises():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)


@pytest.mark.parametrize("number, expected", [
    (2, True),
    (3, False),
    (0, True),
    (-4, True),
    (-7, False),
])
def test_is_even(number, expected):
    assert is_even(number) == expected
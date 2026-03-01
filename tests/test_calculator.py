import pytest
from calculator import Calculator

calc = Calculator()

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
    (2.5, 0.5, 3.0),
])
def test_add(a, b, expected):
    assert calc.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (0, 4, -4),
    (-2, -3, 1),
    (2.5, 0.5, 2.0),
])
def test_subtract(a, b, expected):
    assert calc.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-1, 5, -5),
    (0, 10, 0),
    (2.5, 2, 5.0),
])
def test_multiply(a, b, expected):
    assert calc.multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (4, 2, 2),
    (9, 3, 3),
    (5, 2, 2.5),
])
def test_divide(a, b, expected):
    assert calc.divide(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calc.divide(5, 0)

@pytest.mark.parametrize("n, expected", [
    (2, True),
    (3, True),
    (4, False),
    (17, True),
    (1, False),
    (0, False),
])
def test_is_prime_number(n, expected):
    assert calc.is_prime_number(n) == expected
import pytest
from your_module import safe_divide, advanced_calculator

@pytest.mark.parametrize("a,b,expected", [
    (6, 2, 3.0),
    (5, 0, float('inf')),
    (-10, -2, 5.0)
])
def test_safe_divide(a, b, expected):
    assert safe_divide(a, b) == expected

@pytest.mark.parametrize("a,b,op,expected", [
    (5, 3, "add", 8),
    (5, 3, "sub", 2),
    (5, 3, "mul", 15),
    (6, 2, "div", 3.0),
])
def test_advanced_calculator(a, b, op, expected):
    assert advanced_calculator(a, b, op) == expected

def test_invalid_operation():
    with pytest.raises(ValueError):
        advanced_calculator(5, 3, "mod")

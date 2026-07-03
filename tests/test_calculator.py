"""Tests for calculator module."""

import pytest
from src.calculator import add, divide, multiply, subtract


class TestAdd:
    def test_add_positive(self):
        assert add(2, 3) == 5

    def test_add_negative(self):
        assert add(-1, -1) == -2

    def test_add_mixed(self):
        assert add(-1, 1) == 0

    def test_add_floats(self):
        assert add(1.5, 2.5) == pytest.approx(4.0)


class TestSubtract:
    def test_subtract_positive(self):
        assert subtract(5, 3) == 2

    def test_subtract_negative_result(self):
        assert subtract(3, 5) == -2


class TestMultiply:
    def test_multiply_positive(self):
        assert multiply(3, 4) == 12

    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0


class TestDivide:
    def test_divide_normal(self):
        assert divide(10, 2) == 5.0

    def test_divide_float(self):
        assert divide(7, 2) == pytest.approx(3.5)

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)

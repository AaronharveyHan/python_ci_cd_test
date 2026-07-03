"""A simple calculator package for CI/CD demo."""

from src.calculator import add, divide, multiply, subtract
from src.utils import is_palindrome, reverse_string, word_count

__all__ = [
    "add",
    "divide",
    "is_palindrome",
    "multiply",
    "reverse_string",
    "subtract",
    "word_count",
]

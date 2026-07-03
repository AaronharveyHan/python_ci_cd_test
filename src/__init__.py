"""A simple calculator package for CI/CD demo."""

from src.calculator import add, subtract, multiply, divide
from src.utils import reverse_string, is_palindrome, word_count

__all__ = [
    "add",
    "subtract",
    "multiply",
    "divide",
    "reverse_string",
    "is_palindrome",
    "word_count",
]

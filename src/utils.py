"""Utility functions for string manipulation."""


def reverse_string(s: str) -> str:
    """Return the reversed version of the input string."""
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome (case-insensitive)."""
    cleaned = s.lower().strip()
    return cleaned == cleaned[::-1]


def word_count(s: str) -> int:
    """Return the number of words in the string."""
    return len(s.split())

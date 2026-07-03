"""Tests for utils module."""

from src.utils import is_palindrome, reverse_string, word_count


class TestReverseString:
    def test_reverse(self):
        assert reverse_string("hello") == "olleh"

    def test_reverse_empty(self):
        assert reverse_string("") == ""

    def test_reverse_single(self):
        assert reverse_string("a") == "a"


class TestIsPalindrome:
    def test_palindrome(self):
        assert is_palindrome("racecar") is True

    def test_not_palindrome(self):
        assert is_palindrome("hello") is False

    def test_palindrome_mixed_case(self):
        assert is_palindrome("Racecar") is True


class TestWordCount:
    def test_single_word(self):
        assert word_count("hello") == 1

    def test_multiple_words(self):
        assert word_count("hello world foo") == 3

    def test_empty_string(self):
        assert word_count("") == 0

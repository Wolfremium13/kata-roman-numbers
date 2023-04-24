from assertpy import assert_that

from src.roman_numbers import roman_to_int


class TestRomanNumbersToInteger:
    def test_ignore_empty_roman_number(self):
        assert_that(roman_to_int("")).is_equal_to(0)

    def test_parse_roman_numbers(self):
        assert_that(roman_to_int("I")).is_equal_to(1)
    
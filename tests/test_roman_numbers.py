from assertpy import assert_that

from src.roman_numbers import roman_to_int


class TestRomanNumbersToInteger:
    def test_ignore_empty_roman_number(self):
        assert_that(roman_to_int("")).is_equal_to(0)

    def test_parse_roman_numbers(self):
        assert_that(roman_to_int("I")).is_equal_to(1)
        assert_that(roman_to_int("V")).is_equal_to(5)
        assert_that(roman_to_int("X")).is_equal_to(10)
        assert_that(roman_to_int("L")).is_equal_to(50)
        assert_that(roman_to_int("C")).is_equal_to(100)
        assert_that(roman_to_int("D")).is_equal_to(500)
        assert_that(roman_to_int("M")).is_equal_to(1000)
    
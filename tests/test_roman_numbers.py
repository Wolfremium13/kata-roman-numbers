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

    def test_sum_roman_numbers_with_the_same_letters(self):
        assert_that(roman_to_int("II")).is_equal_to(2)
        assert_that(roman_to_int("III")).is_equal_to(3)
        assert_that(roman_to_int("XX")).is_equal_to(20)
        assert_that(roman_to_int("XXX")).is_equal_to(30)
        assert_that(roman_to_int("CC")).is_equal_to(200)
        assert_that(roman_to_int("CCC")).is_equal_to(300)
        assert_that(roman_to_int("MM")).is_equal_to(2000)
        assert_that(roman_to_int("MMM")).is_equal_to(3000)

    def test_subtract_roman_numbers(self):
        assert_that(roman_to_int("IV")).is_equal_to(4)
        assert_that(roman_to_int("IX")).is_equal_to(9)
        assert_that(roman_to_int("XL")).is_equal_to(40)
        assert_that(roman_to_int("XC")).is_equal_to(90)
        assert_that(roman_to_int("CD")).is_equal_to(400)
        assert_that(roman_to_int("CM")).is_equal_to(900)

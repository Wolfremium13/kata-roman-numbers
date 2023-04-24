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

    def test_sum_roman_numbers_with_different_letters(self):
        assert_that(roman_to_int("VI")).is_equal_to(6)
        assert_that(roman_to_int("VII")).is_equal_to(7)
        assert_that(roman_to_int("VIII")).is_equal_to(8)
        assert_that(roman_to_int("XI")).is_equal_to(11)
        assert_that(roman_to_int("XII")).is_equal_to(12)
        assert_that(roman_to_int("XIII")).is_equal_to(13)
        assert_that(roman_to_int("XIV")).is_equal_to(14)
        assert_that(roman_to_int("XV")).is_equal_to(15)
        assert_that(roman_to_int("XVI")).is_equal_to(16)
        assert_that(roman_to_int("XVII")).is_equal_to(17)
        assert_that(roman_to_int("XVIII")).is_equal_to(18)
        assert_that(roman_to_int("XIX")).is_equal_to(19)
        assert_that(roman_to_int("XXI")).is_equal_to(21)
        assert_that(roman_to_int("XXII")).is_equal_to(22)
        assert_that(roman_to_int("XXIII")).is_equal_to(23)
        assert_that(roman_to_int("XXIV")).is_equal_to(24)
        assert_that(roman_to_int("XXV")).is_equal_to(25)
        assert_that(roman_to_int("XXVI")).is_equal_to(26)
        assert_that(roman_to_int("XXVII")).is_equal_to(27)
        assert_that(roman_to_int("XXVIII")).is_equal_to(28)
        assert_that(roman_to_int("XXIX")).is_equal_to(29)
        assert_that(roman_to_int("XXXI")).is_equal_to(31)
        assert_that(roman_to_int("XXXII")).is_equal_to(32)
        assert_that(roman_to_int("XXXIII")).is_equal_to(33)
        assert_that(roman_to_int("XXXIV")).is_equal_to(34)
        assert_that(roman_to_int("XXXV")).is_equal_to(35)
        assert_that(roman_to_int("XXXVI")).is_equal_to(36)
        assert_that(roman_to_int("XXXVII")).is_equal_to(37)
        assert_that(roman_to_int("XXXVIII")).is_equal_to(38)
        assert_that(roman_to_int("XXXIX")).is_equal_to(39)
        assert_that(roman_to_int("XLIV")).is_equal_to(44)
        assert_that(roman_to_int("XLV")).is_equal_to(45)
        assert_that(roman_to_int("XLVI")).is_equal_to(46)
        assert_that(roman_to_int("XLVII")).is_equal_to(47)
        assert_that(roman_to_int("XLVIII")).is_equal_to(48)
        assert_that(roman_to_int("XLIX")).is_equal_to(49)
        assert_that(roman_to_int("LIV")).is_equal_to(54)
        assert_that(roman_to_int("LV")).is_equal_to(55)
        # TODO: Add more tests
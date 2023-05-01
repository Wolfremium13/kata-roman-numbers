import unittest
import hypothesis.strategies as st
from assertpy import assert_that
from hypothesis import given
import pytest

from src.roman_numbers import ROMAN_NUMBERS, roman_to_int


def test_ignore_empty_roman_number():
    assert_that(roman_to_int("")).is_equal_to(0)


@pytest.mark.parametrize(
    "roman_number, expected",
    [("I", 1), ("V", 5), ("X", 10), ("L", 50), ("C", 100), ("D", 500), ("M", 1000)],
)
def test_parse_roman_numbers(roman_number, expected):
    assert_that(roman_to_int(roman_number)).is_equal_to(expected)


@pytest.mark.parametrize(
    "roman_number, expected",
    [
        ("II", 2),
        ("III", 3),
        ("XX", 20),
        ("XXX", 30),
        ("CC", 200),
        ("CCC", 300),
        ("MM", 2000),
        ("MMM", 3000),
    ],
)
def test_sum_roman_numbers_with_the_same_letters(roman_number, expected):
    assert_that(roman_to_int(roman_number)).is_equal_to(expected)


def test_subtract_roman_numbers():
    assert_that(roman_to_int("IV")).is_equal_to(4)
    assert_that(roman_to_int("IX")).is_equal_to(9)
    assert_that(roman_to_int("XL")).is_equal_to(40)
    assert_that(roman_to_int("XC")).is_equal_to(90)
    assert_that(roman_to_int("CD")).is_equal_to(400)
    assert_that(roman_to_int("CM")).is_equal_to(900)


@given(st.text(alphabet="IVXLCDM", min_size=1, max_size=15))
def test_sum_roman_numbers_with_different_letters(roman_number: str):
    expected = __get_expected_from_roman_number(roman_number)

    assert_that(roman_to_int(roman_number)).is_equal_to(expected)

# This is an anti-pattern, but it's useful to show how to parametrize a test
def __get_expected_from_roman_number(roman_number) -> int:
    expected = 0
    prev_value = 0
    for letter in roman_number:
        value = ROMAN_NUMBERS[letter]
        expected += value - 2 * prev_value if value > prev_value else value
        prev_value = value
    return expected


@pytest.mark.parametrize(
    "roman_number, expected",
    [
        ("I", 1),
        ("IV", 4),
        ("IX", 9),
        ("XII", 12),
        ("XXXVIII", 38),
        ("LXVII", 67),
        ("XCIX", 99),
        ("CDXLIV", 444),
        ("MCMXCVIII", 1998),
    ],
)
def test_sum_roman_numbers_with_different_letters_pytest(roman_number, expected):
    assert_that(roman_to_int(roman_number)).is_equal_to(expected)

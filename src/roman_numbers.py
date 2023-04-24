def roman_to_int(roman_number: str) -> int:
    roman_numbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    return sum(roman_numbers.get(letter, 0) for letter in roman_number)

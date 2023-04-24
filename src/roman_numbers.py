def roman_to_int(roman_number: str) -> int:
    roman_numbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for letter in roman_number:
        if letter not in roman_numbers:
            return 0
        result += roman_numbers[letter]
    return result

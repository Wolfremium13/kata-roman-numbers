ROMAN_NUMBERS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

def roman_to_int(roman_number: str) -> int:
    result = 0
    previous_letter_value = 0
    for letter in roman_number:
        letter_value = ROMAN_NUMBERS.get(letter, 0)
        if letter_value > previous_letter_value:
            result += letter_value - 2 * previous_letter_value
        else:
            result += letter_value
        previous_letter_value = letter_value
    return result

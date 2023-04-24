def roman_to_int(roman_number: str) -> int:
    roman_numbers = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500, 
        "M": 1000
    }
    return 0 if roman_number == "" else roman_numbers[roman_number]

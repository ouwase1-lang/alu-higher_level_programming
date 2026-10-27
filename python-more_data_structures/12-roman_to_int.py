#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
              'C': 100, 'D': 500, 'M': 1000}
    total = 0
    previous = 0
    for ch in reversed(roman_string):
        if ch not in values:
            return 0
        value = values[ch]
        if value < previous:
            total -= value
        else:
            total += value
            previous = value
    return total

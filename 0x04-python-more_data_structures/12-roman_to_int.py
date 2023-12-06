#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D': 500, 'M': 1000}
    total = 0
    for m in range(len(roman_string)):
        if m > 0 and roman_dict[roman_string[m]] > roman_dict[roman_string[m - 1]]:
            total += roman_dict[roman_string[m]] - 2 * roman_dict[roman_string[m - 1]]
        else:
            total += roman_dict[roman_string[m]]
    return total

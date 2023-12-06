#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    madut_dictionary = {}
    for key, value in a_dictionary.items():
        madut_dictionary[key] = value * 2
    return madut_dictionary

#!/usr/bin/python3
def no_c(my_string):
    copy = [m for m in my_string if m.lower() not in ['c', 'C']]
    return ("".join(copy))

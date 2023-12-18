#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for m in range(x):
            print(my_list[m], end="")
            count += 1
    except IndexError:
        pass
    print()
    return count

#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy = []
    for m in range(len(my_list)):
        if my_list[m] == search:
            copy.append(replace)
        else:
            copy.append(my_list[m])
    return copy

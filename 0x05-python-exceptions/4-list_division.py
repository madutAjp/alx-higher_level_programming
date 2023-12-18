#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for m in range(list_length):
        div = 0
        try:
            div = my_list_1[m] / my_list_2[m]
        except (TypeError, ValueError):
            print("wrong type")
        except (ZeroDivisionError, ValueError):
            print("division by 0")
        except (IndexError, ValueError):
            print("out of range")
        finally:
            result.append(div)
    return result

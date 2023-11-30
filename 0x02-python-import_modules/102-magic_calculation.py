#!/usr/bin/python3
if __name__ == "__main__":
    def magic_calculation(a, b):
        add, sub = __import__('magic_calculation_102', fromlist=('add', 'sub'))
        if a < b:
            c = a + b
            for i in range(4, 6):
                c = c + i
                return c
            else:
                return a - b

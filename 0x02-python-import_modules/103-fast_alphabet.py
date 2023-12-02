#!/usr/bin/python3
if __name__ == "__main__":
    print(*list(iter(__import__('string').ascii_uppercase)), sep='')

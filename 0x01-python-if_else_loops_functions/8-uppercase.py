#!/usr/bin/python3
def uppercase(str):
    for string in range(len(str)):
        if ord(str[string]) >= 97 and ord(str[string]) <= 122:
            number = 32
        else:
            number = 0
        print("{:c}".format(ord(str[string]) - number), end='')
    print()

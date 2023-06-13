#!/usr/bin/python3
mumber = (0, 100)
for number in range(0, 100):
    print("{:02}".format(number), end=', ' if number != 99 else '\n')

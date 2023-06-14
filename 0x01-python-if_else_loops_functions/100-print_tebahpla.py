#!/usr/bin/python3
'''
the for iterates range of ASCII codes in reverse from
122('z') down to 64('A'). The -1 step makes it alternate 
UPPER and LOWER while iterating
'''
for a in range(122, 64, -1):
    print("{:c}".format(a), end='')

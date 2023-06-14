#!/usr/bin/python3
'''
looks for numbers in range 97,122 and reverses order
of sequence using the reversed function.
The range 97, 123 contains ASCII code values
I defined a variable 'ASCII' which will take the values
from the range in reverse order
'''
for ASCII in reversed(range(97, 123)):
    '''
    printing the numbers in range in character form
    the ASCII I defined will be printed if it is even, if not,
    it means it is odd, thus subtracts 32 from the value
    Subtracting from 32 changes lowercase ASCII values
    to their corresponding uppercase values
    '''
    print("{:c}".format(ASCII if (ASCII % 2 == 0) else (ASCII - 32)), end='')

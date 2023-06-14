#!/usr/bin/python3
def fizzbuzz():
    # Looking for numbers between 1 and 100
    for numbers in range(1, 101):
        # when the number is a multiple of both 3 and 5, print FizzBuzz
        # the modulus checks for a 0 reminder confirming multiplicity
        if numbers % 3 == 0 and numbers % 5 == 0:
            print("FizzBuzz ", end='')
        # When the number is a multiple of 3, print Fizz
        elif numbers % 3 == 0:
            print("Fizz ", end='')
        # when the num is a multiple of 5, print Buzz
        elif numbers % 5 == 0:
            print("Buzz ", end='')

        else:
            print("{} ".format(numbers), end='')

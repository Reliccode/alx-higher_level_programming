#!/usr/bin/python3
def fizzbuzz():
    for numbers in range(1, 101):
        if numbers % 3 == 0:
            print("Fizz ", end='')
        elif numbers % 5 == 0:
            print("Buzz ", end='')
        else: numbers % 3 == 0 and numbers % 5 == 0
        print("FizzBuzz ", end='')
    print("{} ".format(numbers), end='')

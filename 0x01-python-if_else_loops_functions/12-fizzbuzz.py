#!/usr/bin/python3
def fizzbuzz():
    for numbers in range(0, 101):
        if numbers / 3:
            print("Fizz")
            if numbers / 5:
                print("Buzz")
                if numbers / 5 and 3:
                    print("FizzBuzz")
        else:
            print("{} ".format(numbers), end='')

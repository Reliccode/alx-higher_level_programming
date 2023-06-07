#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print(number, end=" ")
if number > 0:
    print("Positive")
elif number == 0:
    print("Zero")
elif number < 0:
    print("Negative")
else: 
    print("None of the above")


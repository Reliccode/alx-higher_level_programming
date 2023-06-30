#!/usr/bin/python3
class MagicCalculationError(Exception):
    pass

def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if (i > a):
                raise MagicCalculationError("Too far")
            else:
                result += (a ** b) / i
        except MagicCalculationError as e:
            result = b + a
            break
    return (result)

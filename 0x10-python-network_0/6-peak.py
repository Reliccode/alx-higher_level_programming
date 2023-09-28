#!/usr/bin/python3
""" Finds a peak inside a list """


def find_peak(list_of_integers):

    if not list_of_integers:
        return None

    length = len(list_of_integers)
    mid = length // 2
    li = list_of_integers

    if (mid == 0 or li[mid] >= li[mid - 1]) and \
       (mid == length - 1 or li[mid] >= li[mid + 1]):
        return li[mid]

    if mid > 0 and li[mid - 1] > li[mid]:
        return find_peak(li[:mid])
    else:
        return find_peak(li[mid + 1:])

# Example usage:


print(find_peak([1, 2, 4, 6, 3]))

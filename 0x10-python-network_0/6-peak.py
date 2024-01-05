#!/usr/bin/python3
"""
    a function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
        retruns the peak
    """
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        return max(list_of_integers)
    midl = int(len(list_of_integers) / 2)
    peak = list_of_integers[midl]
    if peak > list_of_integers[midl - 1] and peak > list_of_integers[midl + 1]:
        return peak
    elif peak < list_of_integers[midl - 1]:
        return find_peak(list_of_integers[:midl])
    else:
        return find_peak(list_of_integers[midl + 1:])

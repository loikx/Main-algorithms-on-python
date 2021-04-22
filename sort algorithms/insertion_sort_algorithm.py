"""
This file is contained insertion sort algorithm.
Insertion sort has been implemented in the most optimal way.
"""


def insertion_sort(value: list) -> list:
    """
    This function sort python list using the insertion sort algorithm.
    This algorithm is working with O(n^2) asymptotic.
    :param value: input list  with any python types
    :return: new list
    """
    # check type of input value
    if type(value) != list:
        # if not a list than throw the exception
        raise ValueError('value is not a list type object')

    # the first cycle is being needing for take current element
    for i in range(len(value) - 1):
        # the second cycle if being needing for compare current and next elements
        for j in range(i + 1, len(value)):
            # if current value bigger than next
            if value[j] < value[i]:
                # swap it
                value[j], value[i] = value[i], value[j]
    # and return value because i need to pass tests
    # test_for_sort_algorithm.py
    return value
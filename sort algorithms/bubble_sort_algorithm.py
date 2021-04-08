"""
This file is containing bubble sort algorithm ans tests.
Bubble sort has been implemented in the most optimal way.
"""


def bubble_sort(value: list) -> list:
    """
    This function sort python list using the bubble sort algorithm.
    Bubble sort algorithm has asymptotic like O(n^2) in the worst.
    :param array: input list[int/float/str]
    :return: new list[int/float/str]
    """

    # check type of input value
    if type(value) != list:
        # if not a list then throw the exception
        raise ValueError('value is not a list type object')

    # first cycle is being needing for goes along the elements len(a) - 1 times
    for i in range(len(value) - 1):
        # second cycle goes along the elements of list
        for j in range(len(value) - i - 1):
            # if this element less than next
            if value[j] > value[j + 1]:
                # we need to swap elements
                value[j], value[j + 1] = value[j + 1], value[j]
    # and return sorted list
    return value
"""
This file if contained selection sort algorithm.
Selection sort has been implemented in the most optimal way.
"""


def selection_sort(value: list) -> list:
    """
    This function sort python list using the selection sort algorithm.
    This algorithm is working with O(n^2) asymptotic.
    :param value: input list with any python types
    :return: new list
    """

    # check value type
    if type(value) != list:
        # if not a list than throw the exception
        raise ValueError('value is not a list type object')

    # the first cycle is needing for check elements in list
    for i in range(len(value)):
        # remember the index of the current element
        lowest_index = i
        # the second cycle is needed to find the minimum element from the remaining
        for j in range(i + 1, len(value)):
            # looking for the minimum
            if value[j] < value[lowest_index]:
                # remember its index
                lowest_index = j
        # and swap min and current elements
        value[i], value[lowest_index] = value[lowest_index], value[i]
    # return list because we need unittests check
    return value
"""
This file is contained three binary search functions.
search_in checks if the value of the entry is in the array or not
left_boundary this algorithm finds the index of the left entry of an element in an array
right_boundary this algorithm finds the index of the left entry of an element in an array
"""
import unittest
from random import randint


def search_in(array: list, target) -> bool:
    """
    This function is realized algorithm that checks if the value of the entry is in array or not.
    Binary search algorithm is worked with O(logn) asymptotic.
    Array must be SORTED!!!!
    :param array: list[all python types]
    :param target: python type that contained into the array
    :return: bool value (True/False)
    """

    # check array type
    if type(array) != list:
        # throw the exception
        raise ValueError('array is not a list')

    # if array is empty that we know that list is not contained target
    if not array:
        return False

    # initialize low counter
    low_index = 0
    # initialize high counter
    high_index = len(array) - 1

    # algorithm will be work while low <= high
    while low_index <= high_index:
        # create a middle index
        middle_index = (low_index + high_index) // 2
        # check to equal
        if array[middle_index] == target:
            # return the answer
            return True
        # kill one part of array
        elif array[middle_index] > target:
            high_index = middle_index - 1
        # kill other part of array
        else:
            low_index = middle_index + 1

    # return the answer
    return False


def left_boundary(array: list, target) -> int:
    """
    This function search left entry of value.
    Binary search algorithm is worked with O(logn) asymptotic.
    Array must be SORTED!!!!
    :param array: list[all python types]
    :param target: python type that contained into the array
    :return: int (index)
    """

    # check array type
    if type(array) != list:
        # throw the exception
        raise ValueError('array is not a list')

    # is array is empty than return -1
    if not array:
        return -1

    # initialize low counter
    low_index = 0
    # initialize high counter
    high_index = len(array) - 1

    # algorithm will be work while high bigger than low + 1
    while high_index - low_index > 1:
        # create a middle_index
        middle_index = (low_index + high_index) // 2
        if array[middle_index] >= target:
            high_index = middle_index
        else:
            low_index = middle_index

    #  return index
    return high_index


def right_boundary(array: list, target) -> int:
    """
    This function search right entry of value.
    Binary search algorithm is worked with O(logn) asymptotic.
    Array must be SORTED!!!!
    :param array: list[all python types]
    :param target: python type that contained into the array
    :return: int (index)
    """

    # check array type
    if type(array) != list:
        # throw the exception
        raise ValueError('array is not a list')

    # is array is empty than return -1
    if not array:
        return -1

    # initialize low counter
    low_index = 0
    # initialize high counter
    high_index = len(array) - 1

    # algorithm will be work while high bigger than low + 1
    while high_index - low_index > 1:
        # create a middle_index
        middle_index = (low_index + high_index) // 2
        if array[middle_index] > target:
            high_index = middle_index
        else:
            low_index = middle_index

    #  return index
    return high_index
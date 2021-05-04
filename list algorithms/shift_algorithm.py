"""
This file is contained shift algorithm.
This algorithm is worked with O(n) asymptotic.
"""


def left_shift(array: list, steps: int) -> list:
    """
    This function implements the cyclic left shift algorithm.
    This algorithm is worked with O(n) asymptotic.
    :param array: python list with any elements
    :param steps: number of steps
    :return: new list
    """

    # check type of our input value
    if type(array) != list:
        # throw the exception
        raise ValueError('input value is not a list type object')

    # check type of our steps value
    if type(steps) != int:
        # throw the exception
        raise ValueError('input value is not a int type object')

    # check that steps is positive number
    if steps < 0:
        # throw the exception
        raise ValueError('input value must be positive')

    # create a copy of input list
    arr = array[:]

    for i in range(steps):
        # add first element to the end of list
        arr.append(arr.pop(0))

    # return new list
    return arr


def right_shift(array: list, steps: int) -> list:
    """
    This function implements the cyclic right shift algorithm.
    This algorithm is worked with O(n) asymptotic.
    :param array: list[any values]
    :param steps: int
    :return: new list with cycle shift
    """
    # check type of our input value
    if type(array) != list:
        # throw the exception
        raise ValueError('input value is not a list type object')

    # check type of our steps value
    if type(steps) != int:
        # throw the exception
        raise ValueError('input value is not a int type object')

    # check that steps of our steps value
    if steps < 0:
        # throw the exception
        raise ValueError('input value must be positive')

    # create a copy of input list
    arr = array[:]

    for i in range(steps):
        # add last element to first position
        arr.insert(0, arr.pop())

    # return new list
    return arr

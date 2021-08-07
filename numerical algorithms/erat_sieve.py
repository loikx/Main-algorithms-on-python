"""
This file contains eratothenes sieve.
This algorithm search all simple numbers from 1 to number.
"""


def erat_sieve(number: int) -> list[int]:
    """
    This function search all simple numbers between 1 and number and returns array with this numbers.
    :param number: input list with any python types.
    :return: new python list object that contains all simple numbers between 1 to number param.
    """
    if type(number) != int:
        raise ValueError("Number must be integer")

    # initialize array that contains boolean values
    # true - number is simple
    # false - number is not simple
    # we think that we search simple values from 1 to number
    bollen_simple_arr = [True] * number

    # 1 is always not simple number
    bollen_simple_arr[0] = False

    for index in range(1, int(number ** .5) + 1):
        # if current number is simple
        if bollen_simple_arr[index]:
            # we remark all numbers that divides by current number as not simple
            for not_simple_index in range((index + 1) * 2 - 1, number, index + 1):
                bollen_simple_arr[not_simple_index] = False

    # create and return our int array with only simple number
    return [index + 1 for index in range(len(bollen_simple_arr)) if bollen_simple_arr[index]]

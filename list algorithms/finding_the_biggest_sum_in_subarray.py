"""
This file is contained algorithm that find max sum of elements of subarray.
This algorithm is worked with O(n) asymptotic.
"""


def max_summary_of_subarray(array: list[float]) -> float:
    """
    This algorithm is found maximum sum of elements of subarray.
    :param array: list type object
    :return: max sum of elements in subarray
    """
    # check input value type
    if type(array) != list:
        # throw the error
        raise ValueError('Input is not a list type object')

    # check the length of input array
    if not array:
        # if array is empty return 0
        return 0

    # initialize current sum variable
    sum = 0

    # initialize max sum variable
    max_sum = array[0]
    for i in array:
        # add new element to sum
        sum += i
        # choose the max value of new sum last value and this element
        max_sum = max(sum, max_sum, i)
        # choose the max value of new sum and 0
        # we need to do it because our current sum maybe negative
        sum = max(sum, 0)

    # return max_sum value
    return max_sum
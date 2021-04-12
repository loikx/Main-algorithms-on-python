"""
This file is realizing two functions:
merge combine two lists into one
and merge sort sort python with merge sort algorithm.
Merge sort is had asymptotic O(n*logn) in worst.
Ans it's a recursive sort algorithm.
"""


def merge(left_list: list, right_list: list) -> list:
    """
    This function is realizing a merge of two sorted lists.
    :param left_list: left side of the list
    :param right_list: right side of the list
    :return:
    """

    # create supporting list that contain as many elements as left + right lists
    tmp_list = [0] * (len(left_list) + len(right_list))

    # initialize k, n and i counters
    # i is used for counter of left list
    # j is used for counter of right list
    i = j = k = 0

    #
    while i < len(left_list) and j < len(right_list):
        if left_list[i] <= right_list[j]:
            tmp_list[k] = left_list[i]
            i += 1
        else:
            tmp_list[k] = right_list[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(left_list):
        tmp_list[k] = left_list[i]
        k += 1
        i += 1

    # checking if any element was right
    while j < len(right_list):
        tmp_list[k] = right_list[j]
        k += 1
        j += 1

    # return merge list
    return tmp_list


def merge_sort(value: list) -> None:
    """
    This function sort array with merge sort.
    Merge sort is had asymptotic O(logn) in worst.
    :param value: input python list with any elements
    :return: None
    """

    # check type of input value
    if type(value) != list:
        # if not a list than throw the exception
        raise ValueError('value is not a list type object')

    if len(value) <= 1:
        return

    # we take central element
    mid = len(value)//2

    # let's take the first half of the list
    left_list = value[:mid]

    # and then let's take the second half of the list
    right_list = value[mid:]

    # and let's sort the first half
    merge_sort(left_list)

    # then let's sort the second half
    merge_sort(right_list)

    # and merge the sorted lists into one
    tmp_list = merge(left_list, right_list)

    # and then we need to rewrite sort list to the initial
    for i in range(len(value)):
        value[i] = tmp_list[i]

    # i need to return tmp_list because i write tests
    # If you will be use this function than delete this string
    return tmp_list
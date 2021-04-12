"""
This file is containing two quick_sort functions.
quck_sort_with_cycle is needed because its example makes it easier to understand the algorithm
And quick_sort it's a recommended to use in real programs.
Quick sort is a recursive sorting algorithm that sorts a list with asymptotic O (n ^ 2) worst case but O (n*logn) on average case.
"""


def quick_sort_with_cycle(value: list) -> list:
    """
    This function is realizing simple quick_sort algorithm.
    Don't use this version in real programs because it's using append method and for cycles.
    :param value: input list with any python types
    :return: new list
    """

    # check value type
    if type(value) != list:
        # if not a list than throw the exception
        raise ValueError('value is not a list')

    # quick sort is a recursive algorithm
    # and we have to check the edge case
    if len(value) <= 1:
        # if we do not have elements to sort
        # then return the value
        return value

    # if we have elements to sort
    # Then we need to search a barrier element
    barrier_element = value[len(value) // 2]

    # and initialize 3 python lists
    # first for elements that smaller than barrier
    list_of_smaller_elements = []
    # second for elements that equal than barrier
    list_of_equal_elements = []
    # and third for elements that bigger than barrier
    list_of_bigger_elements = []

    # first cycle is needed for fill the list with elements that smaller than barrier_element
    for i in value:
        if i < barrier_element:
            list_of_smaller_elements.append(i)

    # second cycle is needed for fill the list with elements that equal than barrier_element
    for i in value:
        if i == barrier_element:
            list_of_equal_elements.append(i)

    # third cycle if needed for fill the list with elements that bigger than barrier_element
    for i in value:
        if i > barrier_element:
            list_of_bigger_elements.append(i)

    # and recursive return with concatenation of three sorted list
    return quick_sort(list_of_smaller_elements) + list_of_equal_elements + quick_sort(list_of_bigger_elements)


def quick_sort(value: list) -> list:
    """
    This function implements the quick sort algorithm at its best.
    :param value: input list with any python types
    :return: new list
    """

    # check value type
    if type(value) != list:
        # if not a list than throw the exception
        raise ValueError('value is not a list')

    # quick sort is a recursive algorithm
    # and we have to check the edge case
    if len(value) <= 1:
        # if we do not have elements to sort
        # then return the value
        return value

    # if we have elements to sort
    # Then we need to search a barrier element
    barrier_element = value[len(value) // 2]

    # at first we create a list that contain elements smaller than barrier_element
    list_of_smaller_elements = [i for i in value if i < barrier_element]

    # at second we create a list that contain elements equal to barrier_element
    list_of_equal_elements = [i for i in value if i == barrier_element]

    # at third we create a list that contain elements bigger than barrier_element
    list_of_bigger_elements = [i for i in value if i > barrier_element]

    # and recursive return with concatenation of three sorted list
    return quick_sort(list_of_smaller_elements) + list_of_equal_elements + quick_sort(list_of_bigger_elements)

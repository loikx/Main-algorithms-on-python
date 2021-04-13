"""
This file is containing translate roman numerals to arabic algorithm.
This algorithm is working with time O(n).
But only for nums into 1 <= n <= 3000 range.
"""


def roman_to_arabic(roman_string: str) -> int:
    """
    This function is realizing roman_to_arabic translate algorithm.
    This algorithm is working correct only for  1 <= digits <= 3000.
    :param roman_string: input str python type object that consist only roman nums
    :return: int value that equal to roman value
    """
    # check input value type
    if type(roman_string) != str:
        # throw the exception
        raise ValueError('input value is not a str python type')

    # initialize arabic answer
    arabic_value = 0
    # initialize help string

    tmp_string = roman_string + '0'

    # initialize dict with all roman nums
    to_roman_keys = {
        "0": 0,
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    # initialize counter
    i = 1

    while i < len(tmp_string):
        # if next value is bigger than past
        if to_roman_keys[tmp_string[i - 1]] < to_roman_keys[tmp_string[i]]:
            # that we need to add into our sum quotient of this and old value
            arabic_value += to_roman_keys[tmp_string[i]] - to_roman_keys[tmp_string[i - 1]]
            # and jump through two numbers
            i += 2
        # if next value is smaller than this
        else:
            # we need to add old value into arabic sum
            arabic_value += to_roman_keys[tmp_string[i - 1]]
            # and jump through the one number
            i += 1

    # and return our integer value
    return arabic_value
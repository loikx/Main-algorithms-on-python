def gcd(a: int, b: int) -> int:
    """
    This function finds maximum common divisor and returns it.
    :param a: the first number for which you want to get the maximum common divisor
    :param b: the second number for which you want to get the maximum common divisor
    :return: int value
    """
    # we need to get zero remainder of the division
    while a != 0 and b != 0:
        # we need to divide the max value
        if a > b:
            a %= b
        else:
            b %= a
    # and then sum two remainders of the division
    return a + b


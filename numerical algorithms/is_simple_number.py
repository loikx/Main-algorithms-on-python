def is_simple(number: int) -> bool:
    """
    This function defines simple number or not and returns boolean value.
    :param number: integer value
    :return: boolean value (True if number is simple else False
    """

    # we need to check all values smaller than sqrt from number
    for i in range(2, int(number ** .5) + 1):
        # if number is divided by i than number is not simple
        if number % i == 0:
            return False
    # else if number is not divided by all value from 2 to sqrt(number) than number is simple
    return True


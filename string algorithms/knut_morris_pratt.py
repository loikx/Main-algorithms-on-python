def prefix(string: str) -> list[int]:
    """
    This function provides prefix function that we need to use in knut-morris-pratt algorithm.
    """
    Pi = [0] * len(string)

    for i in range(1, len(string)):
        p = Pi[i - 1]
        while p > 0 and string[i] != string[p]:
            p = Pi[p - 1]
        if string[p] == string[i]:
            p += 1
        Pi[i] = p

    return Pi


def knut_morris_pratt(string: str, subString: str) -> bool:
    """
    This function provides an algorithm that checks string to have subString.
    THIS ALGORITHMS WORKS IF YOUR STRING DOES NOT HAVE # symbol.
    :param string: str type python object, string in which we need to find substring
    :param subString: str type python object, substring that we need to find in string
    :return: boolean value (True is subString in string else False)
    """
    # first of all we need to add special symbol between string and subString
    st = subString + '#' + string

    for i in prefix(st):
        # if we find substring with len like our
        # than we find our substring
        if i == len(subString):
            return True

    return False


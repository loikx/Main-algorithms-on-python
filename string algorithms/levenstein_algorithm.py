def levenstein(string1: str, string2: str) -> int:
    """
    This function finds min way to get from string1 string2.
    :param string1: str python object
    :param string2: str python object
    :return: int value - length of this way
    """
    # we need to get help with array
    # he has len(string2) + 1 columns and len(string1) + 1 rows
    tmp = [[i + j if i * j == 0 else 0 for j in range(len(string2) + 1)] for i in range(len(string1) + 1)]

    # we need to start cycled from first to the end
    # cause zero elements it's our extreme cases
    for i in range(1, len(string1) + 1):
        for j in range(1, len(string2) + 1):
            # if string1 and string2 elements is equal
            if string1[i - 1] == string2[j - 1]:
                # we don't need to change our words
                # than we get our last min length
                tmp[i][j] = tmp[i - 1][j - 1]
            else:
                # if elements are not equal
                # we know that 1 change we need to do
                # and sum it with min way to the other changes
                # tmp[i - 1][j - 1] we change element in string1 and string2
                # tmp[i - 1][j] we delete element from string1
                # tmp[i][j - 1] we delete element from string2
                tmp[i][j] = 1 + min(tmp[i - 1][j - 1], tmp[i - 1][j], tmp[i][j - 1])

    # and value in last row and last column is our min length
    return tmp[-1][-1]

def lcs_len(arr1: list[float], arr2: list[float]) -> int:
    """
    This function finds len of the largest common subarray in arr1 and arr2.
    :param arr1: list[int/float]
    :param arr2: list[int/float]
    :return: int value - max len of the common subarray
    """

    # we need to get help with third array
    # he has len(arr2) + 1 columns and len(arr1) + 1 rows
    tmp = [[0] * (len(arr2) + 1) for _ in range(len(arr1) + 1)]

    # we need to start cycled from first to the end
    # cause zero elements it's our extreme cases
    for i in range(1, len(arr1) + 1):
        for j in range(1, len(arr2) + 1):
            # if arr1 and arr2 elements is equal
            if arr1[i - 1] == arr2[j - 1]:
                # we sum our last max len and 1
                tmp[i][j] = 1 + tmp[i - 1][j - 1]
            else:
                # if elements are not equal we get our last max length of the subsequence
                tmp[i][j] = max(tmp[i - 1][j], tmp[i][j - 1])
    # and element in last row and last column is our max length
    return tmp[-1][-1]


def lcs_arr(arr1: list[float], arr2: list[float]) -> list[float]:
    """
    This function finds len of the largest common subarray in arr1 and arr2.
    :param arr1: list[int/float]
    :param arr2: list[int/float]
    :return: list[int/float] with the way to the largest common subsequence
    """
    # we need to get help with third array
    # he has len(arr2) + 1 columns and len(arr1) + 1 rows
    tmp = [[[]] * (len(arr2) + 1) for _ in range(len(arr1) + 1)]

    # we need to start cycled from first to the end
    # cause zero elements it's our extreme cases
    for i in range(1, len(arr1) + 1):
        for j in range(1, len(arr2) + 1):
            # if arr1 and arr2 elements is equal
            if arr1[i - 1] == arr2[j - 1]:
                # we concatenate our last largest subsequence and new element
                tmp[i][j] = [arr1[i - 1]] + tmp[i - 1][j - 1]
            else:
                # if elements are not equal we get our last subsequence
                tmp[i][j] = max(tmp[i - 1][j], tmp[i][j - 1])
    # and array in last row and last column is our max length
    return tmp[-1][-1]



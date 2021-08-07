"""
This file is contained function that add two nums with long add algorithm and some simple tests.
This algorithm is working with O(n * m) asymptotic.
"""
import unittest
import random


def add_two_numbers(array1: list[int], array2: list[int]) -> list[int]:
    """
    This function is contained algorithm that realize add of two long nums.
    This algorithm has asymptotic O(n * m).
    :param array1: list[int]
    :param array2: list[int]
    :return: list[int]
    """

    # check array1 and array2 types
    if type(array1) != list or type(array2) != list:
        # they must be int
        raise ValueError('args is not a list type object')

    # check length of array1 and array2
    if len(array1) == 0 or len(array2) == 0:
        # return concatenated of two list if one of them has not have elements
        return array1 + array2

    # check type of elements into array1 and array2
    # check two lists
    if type(array2[0]) != int or type(array1[0]) != int:
        # throw the exception
        raise ValueError('list values is not int type')

    # create new list
    ans = [0] * (max(len(array1), len(array2)) + 1)
    # initialize len counter
    i = 0

    # fill in the shortest array
    while i < min(len(array1), len(array2)):
        # sum three numbers
        ans[i] += array1[i] + array2[i]
        # add to the next overflow
        ans[i + 1] += ans[i] // 10
        # and take the remainder for the current nums
        ans[i] %= 10
        i += 1

    # check array1
    while i < len(array1):
        ans[i] += array1[i]
        ans[i + 1] += ans[i] // 10
        ans[i] %= 10
        i += 1

    # check array2
    while i < len(array2):
        ans[i] += array2[i]
        ans[i + 1] += ans[i] // 10
        ans[i] %= 10
        i += 1

    # check that the last elements are not zero
    while ans[-1] == 0 and len(ans) > 1:
        ans.pop()

    # return sum of two numbers
    return ans


class TestCases(unittest.TestCase):
    """This class is realized tests of add_two_numbers function"""

    def test_with_equal_len(self):
        """
        This method is realized 100 tests with one length of nums. (len=500).
        """
        for i in range(100):
            a = []
            b = []
            for j in range(500):
                # create two random numbers
                a.append(random.randint(0, 9))
                b.append(random.randint(0, 9))
            a1 = int(''.join(list(map(str, a))))
            b1 = int(''.join(list(map(str, b))))
            # create sum of our numbers
            right_ans = list(map(int, list(''.join(map(str, list(str(a1 + b1)))))))
            # reverse it
            a.reverse()
            b.reverse()
            right_ans.reverse()
            # check to equal
            self.assertEqual(add_two_numbers(a, b), right_ans)

    def test_with_not_equal_len(self):
        """
        This method is realized 100 tests with different length of nums.
        """
        for i in range(100):
            a = []
            b = []
            for j in range(50):
                # create first list with 1-50 elements
                a.append(random.randint(0, 9))
                for k in range(50):
                    # create second list with 50 elements
                    b.append(random.randint(0, 9))
                a1 = int(''.join(list(map(str, a))))
                b1 = int(''.join(list(map(str, b))))
                # create sum of our numbers
                right_ans = list(map(int, list(''.join(map(str, list(str(a1 + b1)))))))
                # reverse it
                a.reverse()
                b.reverse()
                right_ans.reverse()
                # check to equal
                self.assertEqual(add_two_numbers(a, b), right_ans)


if __name__ == '__main__':
    unittest.main()

"""
This file contains fast_pow function that provides fats pow algorithm.
"""
import unittest


def fast_pow(base: int, power: int) -> int:
    """
    This function raises a base number to a power.
    This function used fast pow algorithm, that work with recursive.
    :param base: number that function will raises to a  power
    :param power: a power to which number will be raised.
    :return: int result
    """
    if type(base) != int or type(power) != int:
        raise ValueError('Base and power must be integers')

    # extreme situation
    if power == 0:
        return 1

    # if current power divides by two
    if power % 2 == 0:
        # that we need to pow base to a power divides by 2 and call fast_pow with new parameters
        return fast_pow(base ** 2, power // 2)

    # else we need to call fast_pow with power - 1 parameter
    return base * fast_pow(base, power - 1)


class TestFastPow(unittest.TestCase):
    def setUp(self) -> None:
        self.number_array = list(range(1000))
        self.pow_array = list(range(10))

    def test_fast_pow(self):
        for i in self.number_array:
            for j in self.pow_array:
                self.assertEqual(i ** j, fast_pow(i, j))


if __name__ == '__main__':
    unittest.main()

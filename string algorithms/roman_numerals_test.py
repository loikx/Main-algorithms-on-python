import unittest
from roman_numerals_to_arabic_algorithm import roman_to_arabic
"""
This file is containing checkio function from https://habr.com/ru/post/311678/
"""


def checkio(n:int) -> str:
    pool = "m2d5c2l5x2v5i"
    rep = lambda t: int(pool[t - 1])

    def roman(n, j=0, v=1000):
        while True:
            while n >= v: yield pool[j]; n -= v
            if n <= 0: return
            k = j + 2; u = v // rep(k)
            if rep(k) == 2: k += 2; u //= rep(k)
            if n + u >= v: yield pool[k]; n += u
            else: j += 2; v //= rep(j)

    return "".join(roman(n)).upper()


class TestCases(unittest.TestCase):
    """
    This class is used unittest for check function roman_to_arabic.
    """
    def tests(self):
        """
        This function is realizing test using unittest.
        test_dict is containing only str keys and int integers.
        keys is a roman nums.
        """
        for i in range(3000):
            self.assertEqual(roman_to_arabic(checkio(i)), i)


if __name__ == "__main__":
    unittest.main()
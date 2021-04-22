import unittest

"""
This file is contained function that check string to palindrome.
"""


def is_palindrome(s: str) -> bool:
    """
    This function is realizing algorithm that check string  to palindrome.
    :param s: input string object
    :return: True or False
    """
    # at first we need to import string module
    import string

    # we need to initialize help_s because we don't want to touch input string
    help_s = s

    # and we need to delete all punctuation marks
    for i in string.punctuation + '—':
        # i will be use replace method because it's not bad
        help_s = help_s.replace(i, '')

    # and we need to replace all empty positions
    help_s = help_s.replace(" ", '')

    # and at the end we need to make the string lowercase
    help_s = help_s.lower()

    # and return the equality of the two strings
    return help_s[::-1] == help_s


class TestsCases(unittest.TestCase):
    """
    This class is used unittests for is_palindrome function.
    """

    def setUp(self):
        self.is_palindrome = is_palindrome

    def tests(self):
        a = ['Лёша на полке клопа нашёл',
             'А роза упала на лапу Азора',
             'Я - арка кр&*)($%^*&а_я',
             'О, лета тело!',
             'Кони,(&@%#^%$!@+!@ то!)(*@&^%$#@%@пот, инок',
             'Шла !&@@Маша по шоссе и с!@&612осала суш&*#^%$@#$!ку']
        for i in range(len(a)):
            if i < 5:
                self.assertTrue(self.is_palindrome(a[i]))
            else:
                self.assertFalse(self.is_palindrome(a[i]))


if __name__ == '__main__':
    unittest.main()
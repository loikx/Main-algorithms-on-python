import unittest
import random
from bubble_sort_algorithm import bubble_sort
from selection_sort_algorithm import selection_sort
# from quick_sort_algorithm import quick_sort
# from insertion_sort_algorithm import insertion_sort


class TestCases(unittest.TestCase):
    """
    Change the name of algorithm in method setUp if you don't want to test bubble sort algorithm.
    """
    def setUp(self):
        self.sort_name = selection_sort

    def test_with_int_elements(self):
        """
        This function is realizing test using unittest.
        test_array is containing only int non negative values in range from -500 to 500.
        :sort_name: function
        """
        test_array = []
        for i in range(1000):
            test_array.append(random.randint(-500, 500))
        equivalent_array = test_array.copy()
        equivalent_array.sort()
        for i in range(10):
            random.shuffle(test_array)
            self.assertEqual(self.sort_name(test_array), equivalent_array)

    def test_with_float_elements(self):
        """
        This function is realizing test using unittest.
        test_array is containing only float non negative values in range from -500 to 500.
        :sort_name: function
        """
        test_array = []
        for i in range(1000):
            test_array.append(random.uniform(-500, 500))
        equivalent_array = test_array.copy()
        equivalent_array.sort()
        for i in range(10):
            random.shuffle(test_array)
            self.assertEqual(self.sort_name(test_array), equivalent_array)

    def test_with_str_elements(self):
        """
        This function is realizing test using unittest.
        test_array is containing only str objects.
        :sort_name: function
        """
        test_array = list('abcdefghijklmnopqrstuvwxyz')
        equivalent_array = list('abcdefghijklmnopqrstuvwxyz')
        for i in range(10):
            random.shuffle(test_array)
            self.assertEqual(self.sort_name(test_array), equivalent_array)

    def test_with_int_and_float_elements(self):
        """
        This function is realizing test using unittest.
        test_array is containing int and float objects in range from -500 to 500.
        :sort_name: function
        """
        test_array = []
        for i in range(500):
            test_array.append(random.randint(-500, 500))
        for i in range(500):
            test_array.append(random.uniform(-500, 500))
        equivalent_array = test_array.copy()
        equivalent_array.sort()
        for i in range(10):
            random.shuffle(test_array)
            self.assertEqual(self.sort_name(test_array), equivalent_array)


if __name__ == '__main__':
    unittest.main()
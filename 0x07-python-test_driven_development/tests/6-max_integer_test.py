#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def setUp(self):
        """
        Set up different test lists before each test.
        """
        self.list = [1, 2]
        self.mixed_numbers = [-1, 5, 0, 3.5, -2]

    def test_list_type(self):
        """
        Test that the type of the list is list and the max function works
        correctly.
        """
        self.assertIsInstance(self.list, list)
        self.assertEqual(max_integer(self.list), 2)

    def test_max_value(self):
        """Test max value in a given list."""

        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer([42]), 42)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer(self.mixed_numbers), 5)
        self.assertEqual(max_integer([5, 5, 5]), 5)
        self.assertEqual(max_integer([0, -1, -2]), 0)

    def test_type_elements(self):
        """Test that all elements in the list are numbers (int or float)"""

        for i in self.list:
            self.assertIsInstance(i, (int, float))
        for i in self.mixed_numbers:
            self.assertIsInstance(i, (int, float))

    def test_none(self):
        """Test passing None as an argument should raise TypeError"""

        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == "__main__":
    unittest.main()

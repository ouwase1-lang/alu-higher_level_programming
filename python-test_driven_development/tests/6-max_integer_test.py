#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function."""

    def test_ordered_list(self):
        """The max is at the end."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """The max is in the middle."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """The max is the first element."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_one_element(self):
        """A list with a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """An empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """No argument returns None."""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """All numbers are negative."""
        self.assertEqual(max_integer([-4, -1, -3]), -1)

    def test_mixed_signs(self):
        """Positive, negative and zero values."""
        self.assertEqual(max_integer([-5, 0, 5]), 5)

    def test_duplicates(self):
        """The max appears more than once."""
        self.assertEqual(max_integer([2, 9, 9, 1]), 9)

    def test_floats(self):
        """Floats and integers together."""
        self.assertEqual(max_integer([1.5, 3, 2.9]), 3)

    def test_string(self):
        """A string returns its greatest character."""
        self.assertEqual(max_integer("abc"), "c")

    def test_list_of_strings(self):
        """A list of strings returns the greatest one."""
        self.assertEqual(max_integer(["apple", "pear"]), "pear")

    def test_incompatible_types(self):
        """Comparing a string with an integer raises TypeError."""
        with self.assertRaises(TypeError):
            max_integer([1, "2"])

    def test_none(self):
        """None raises TypeError."""
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == "__main__":
    unittest.main()

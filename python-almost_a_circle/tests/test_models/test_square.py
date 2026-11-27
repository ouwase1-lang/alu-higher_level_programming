#!/usr/bin/python3
"""Unit tests for the Square class."""
import contextlib
import io
import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for the Square class."""

    def setUp(self):
        """Reset the object counter."""
        Base._Base__nb_objects = 0

    def test_inherits_rectangle(self):
        """Square is a Rectangle."""
        self.assertIsInstance(Square(1), Rectangle)

    def test_attributes(self):
        """Arguments are assigned."""
        s = Square(5, 1, 2, 3)
        self.assertEqual((s.size, s.width, s.height, s.x, s.y, s.id),
                         (5, 5, 5, 1, 2, 3))

    def test_automatic_id(self):
        """Ids are automatic."""
        self.assertEqual([Square(1).id, Square(1).id], [1, 2])

    def test_validation(self):
        """Errors match the Rectangle ones."""
        cases = [
            (("1",), TypeError, "width must be an integer"),
            ((0,), ValueError, "width must be > 0"),
            ((1, "2"), TypeError, "x must be an integer"),
            ((1, -1), ValueError, "x must be >= 0"),
            ((1, 1, "3"), TypeError, "y must be an integer"),
            ((1, 1, -1), ValueError, "y must be >= 0"),
        ]
        for args, error, message in cases:
            with self.subTest(args=args):
                with self.assertRaisesRegex(error, message):
                    Square(*args)

    def test_size_setter(self):
        """The size sets both sides."""
        s = Square(5)
        s.size = 10
        self.assertEqual((s.width, s.height), (10, 10))

    def test_size_setter_validation(self):
        """The size setter uses the width messages."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5).size = "9"
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(5).size = -1

    def test_str(self):
        """The string representation is correct."""
        self.assertEqual(str(Square(3, 1, 3, 9)), "[Square] (9) 1/3 - 3")

    def test_area_and_display(self):
        """Inherited methods work."""
        s = Square(2, 2)
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            s.display()
        self.assertEqual(s.area(), 4)
        self.assertEqual(buffer.getvalue(), "  ##\n  ##\n")

    def test_update_args(self):
        """Positional arguments are assigned in order."""
        s = Square(5)
        s.update(10, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (10) 3/4 - 2")

    def test_update_kwargs(self):
        """Keyword arguments are assigned."""
        s = Square(5)
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 0/1 - 7")
        self.assertEqual(s.height, 7)

    def test_update_args_over_kwargs(self):
        """Keywords are skipped when positional arguments exist."""
        s = Square(5)
        s.update(10, size=7)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 5")

    def test_update_validation(self):
        """Update validates the values."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(5).update(1, 0)

    def test_to_dictionary(self):
        """The dictionary holds id, size, x and y."""
        self.assertEqual(Square(10, 2, 1, 4).to_dictionary(),
                         {"id": 4, "size": 10, "x": 2, "y": 1})


if __name__ == "__main__":
    unittest.main()

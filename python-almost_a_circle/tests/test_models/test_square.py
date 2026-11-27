#!/usr/bin/python3
"""Unit tests for the Square class."""
import contextlib
import io
import os
import tempfile
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


class TestSquareCalls(unittest.TestCase):
    """Explicit Square calls, one case at a time."""

    def setUp(self):
        """Reset the counter and use an empty temporary directory."""
        Base._Base__nb_objects = 0
        self.old_directory = os.getcwd()
        self.directory = tempfile.TemporaryDirectory()
        os.chdir(self.directory.name)

    def tearDown(self):
        """Return to the original directory."""
        os.chdir(self.old_directory)
        self.directory.cleanup()

    def test_one_argument(self):
        """Check one argument."""
        self.assertEqual(Square(1).size, 1)

    def test_two_arguments(self):
        """Check two arguments."""
        self.assertEqual(Square(1, 2).x, 2)

    def test_three_arguments(self):
        """Check three arguments."""
        self.assertEqual(Square(1, 2, 3).y, 3)

    def test_four_arguments(self):
        """Check four arguments."""
        self.assertEqual(Square(1, 2, 3, 4).id, 4)

    def test_string_size(self):
        """Check string size."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")

    def test_string_x(self):
        """Check string x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")

    def test_string_y(self):
        """Check string y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

    def test_negative_size(self):
        """Check negative size."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_zero_size(self):
        """Check zero size."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_negative_x(self):
        """Check negative x."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)

    def test_negative_y(self):
        """Check negative y."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)

    def test_save_to_file_none(self):
        """Check save to file none."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        """Check save to file empty."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_one(self):
        """Check save to file one."""
        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as f:
            self.assertEqual(len(Square.from_json_string(f.read())), 1)

    def test_load_from_file_missing(self):
        """Check load from file missing."""
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_existing(self):
        """Check load from file existing."""
        Square.save_to_file([Square(1)])
        loaded = Square.load_from_file()
        self.assertIsInstance(loaded[0], Square)

    def test_update_empty(self):
        """Check update empty."""
        item = Square(5)
        before = str(item)
        item.update()
        self.assertEqual(str(item), before)

    def test_update_args_1(self):
        """Check update args 1."""
        item = Square(5)
        item.update(89)
        self.assertEqual(item.id, 89)

    def test_update_kwargs_1(self):
        """Check update kwargs 1."""
        item = Square(5)
        item.update(**{"id": 89})
        self.assertEqual(item.id, 89)

    def test_create_1(self):
        """Check create 1."""
        item = Square.create(**{"id": 89})
        self.assertEqual(item.id, 89)

    def test_update_args_2(self):
        """Check update args 2."""
        item = Square(5)
        item.update(89, 1)
        self.assertEqual(item.id, 89)
        self.assertEqual(item.size, 1)

    def test_update_kwargs_2(self):
        """Check update kwargs 2."""
        item = Square(5)
        item.update(**{"id": 89, "size": 1})
        self.assertEqual(item.id, 89)
        self.assertEqual(item.size, 1)

    def test_create_2(self):
        """Check create 2."""
        item = Square.create(**{"id": 89, "size": 1})
        self.assertEqual(item.id, 89)
        self.assertEqual(item.size, 1)

    def test_update_args_3(self):
        """Check update args 3."""
        item = Square(5)
        item.update(89, 1, 2)
        self.assertEqual(item.id, 89)
        self.assertEqual(item.size, 1)
        self.assertEqual(item.x, 2)

    def test_update_kwargs_3(self):
        """Check update kwargs 3."""
        item = Square(5)
        item.update(**{"id": 89, "size": 1, "x": 2})
        self.assertEqual(item.id, 89)
        self.assertEqual(item.size, 1)
        self.assertEqual(item.x, 2)

    def test_create_3(self):
        """Check create 3."""
        item = Square.create(**{"id": 89, "size": 1, "x": 2})
        self.assertEqual(item.id, 89)
        self.assertEqual(item.size, 1)
        self.assertEqual(item.x, 2)

    def test_update_args_4(self):
        """Check update args 4."""
        item = Square(5)
        item.update(89, 1, 2, 3)
        self.assertEqual(item.id, 89)
        self.assertEqual(item.size, 1)
        self.assertEqual(item.x, 2)
        self.assertEqual(item.y, 3)

    def test_update_kwargs_4(self):
        """Check update kwargs 4."""
        item = Square(5)
        item.update(**{"id": 89, "size": 1, "x": 2, "y": 3})
        self.assertEqual(item.id, 89)
        self.assertEqual(item.size, 1)
        self.assertEqual(item.x, 2)
        self.assertEqual(item.y, 3)

    def test_create_4(self):
        """Check create 4."""
        item = Square.create(**{"id": 89, "size": 1, "x": 2, "y": 3})
        self.assertEqual(item.id, 89)
        self.assertEqual(item.size, 1)
        self.assertEqual(item.x, 2)
        self.assertEqual(item.y, 3)


if __name__ == "__main__":
    unittest.main()

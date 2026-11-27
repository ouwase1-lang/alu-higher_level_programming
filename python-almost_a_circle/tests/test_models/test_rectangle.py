#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import contextlib
import io
import os
import tempfile
import unittest

from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInit(unittest.TestCase):
    """Tests for instantiation and validation."""

    def setUp(self):
        """Reset the object counter."""
        Base._Base__nb_objects = 0

    def test_inherits_base(self):
        """Rectangle is a Base."""
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_ids(self):
        """Ids are automatic unless given."""
        self.assertEqual(Rectangle(10, 2).id, 1)
        self.assertEqual(Rectangle(2, 10).id, 2)
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)

    def test_attributes(self):
        """Arguments are assigned."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id),
                         (1, 2, 3, 4, 5))

    def test_default_offsets(self):
        """x and y default to 0."""
        r = Rectangle(1, 2)
        self.assertEqual((r.x, r.y), (0, 0))

    def test_missing_arguments(self):
        """Width and height are required."""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_private_attributes(self):
        """Attributes are private."""
        with self.assertRaises(AttributeError):
            Rectangle(1, 2).__width

    def test_not_integers(self):
        """Non integers raise TypeError for every attribute."""
        for name in ("width", "height", "x", "y"):
            for value in ("2", 2.5, None, {}, [], True):
                with self.subTest(name=name, value=value):
                    message = "^{} must be an integer$".format(name)
                    with self.assertRaisesRegex(TypeError, message):
                        setattr(Rectangle(1, 1), name, value)

    def test_size_not_positive(self):
        """Width and height must be greater than 0."""
        for name in ("width", "height"):
            for value in (0, -10):
                with self.subTest(name=name, value=value):
                    message = "^{} must be > 0$".format(name)
                    with self.assertRaisesRegex(ValueError, message):
                        setattr(Rectangle(1, 1), name, value)

    def test_negative_offsets(self):
        """x and y must not be negative."""
        for name in ("x", "y"):
            with self.subTest(name=name):
                message = "^{} must be >= 0$".format(name)
                with self.assertRaisesRegex(ValueError, message):
                    setattr(Rectangle(1, 1), name, -1)

    def test_constructor_validation(self):
        """The constructor validates its arguments."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)


class TestRectangleMethods(unittest.TestCase):
    """Tests for the public methods."""

    def setUp(self):
        """Reset the object counter."""
        Base._Base__nb_objects = 0

    def output(self, rectangle):
        """Return what display prints."""
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            rectangle.display()
        return buffer.getvalue()

    def test_area(self):
        """The area is width times height."""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_display(self):
        """The rectangle is drawn."""
        self.assertEqual(self.output(Rectangle(2, 2)), "##\n##\n")

    def test_display_offsets(self):
        """x and y shift the drawing."""
        self.assertEqual(self.output(Rectangle(2, 3, 2, 2)),
                         "\n\n  ##\n  ##\n  ##\n")
        self.assertEqual(self.output(Rectangle(3, 2, 1, 0)), " ###\n ###\n")

    def test_str(self):
        """The string representation is correct."""
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)),
                         "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        """Positional arguments are assigned in order."""
        values = (89, 2, 3, 4, 5)
        expected = ["10/10 - 10/10", "10/10 - 2/10", "10/10 - 2/3",
                    "4/10 - 2/3", "4/5 - 2/3"]
        for count, text in enumerate(expected, 1):
            with self.subTest(count=count):
                r = Rectangle(10, 10, 10, 10)
                r.update(*values[:count])
                self.assertEqual(str(r), "[Rectangle] (89) " + text)

    def test_update_nothing(self):
        """No argument changes nothing."""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

    def test_update_extra_args(self):
        """Extra positional arguments are ignored."""
        r = Rectangle(1, 1)
        r.update(89, 2, 3, 4, 5, 6)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """Keyword arguments are assigned."""
        r = Rectangle(10, 10, 10, 10)
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/10")

    def test_update_args_over_kwargs(self):
        """Keywords are skipped when positional arguments exist."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, height=1)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_validation(self):
        """Update validates the values."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(1, 1).update(1, 0)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1).update(x="1")

    def test_to_dictionary(self):
        """The dictionary holds every attribute."""
        self.assertEqual(Rectangle(10, 2, 1, 9, 5).to_dictionary(),
                         {"id": 5, "width": 10, "height": 2, "x": 1, "y": 9})


class TestRectangleCalls(unittest.TestCase):
    """Explicit Rectangle calls, one case at a time."""

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

    def test_two_arguments(self):
        """Check two arguments."""
        self.assertEqual(Rectangle(1, 2).height, 2)

    def test_three_arguments(self):
        """Check three arguments."""
        self.assertEqual(Rectangle(1, 2, 3).x, 3)

    def test_four_arguments(self):
        """Check four arguments."""
        self.assertEqual(Rectangle(1, 2, 3, 4).y, 4)

    def test_five_arguments(self):
        """Check five arguments."""
        self.assertEqual(Rectangle(1, 2, 3, 4, 5).id, 5)

    def test_string_width(self):
        """Check string width."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)

    def test_string_height(self):
        """Check string height."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")

    def test_string_x(self):
        """Check string x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3")

    def test_string_y(self):
        """Check string y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")

    def test_negative_width(self):
        """Check negative width."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_negative_height(self):
        """Check negative height."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)

    def test_zero_width(self):
        """Check zero width."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_zero_height(self):
        """Check zero height."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)

    def test_negative_x(self):
        """Check negative x."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3)

    def test_negative_y(self):
        """Check negative y."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -4)

    def test_save_to_file_none(self):
        """Check save to file none."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        """Check save to file empty."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_one(self):
        """Check save to file one."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(Rectangle.from_json_string(f.read())), 1)

    def test_load_from_file_missing(self):
        """Check load from file missing."""
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_existing(self):
        """Check load from file existing."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        loaded = Rectangle.load_from_file()
        self.assertIsInstance(loaded[0], Rectangle)

    def test_update_empty(self):
        """Check update empty."""
        item = Rectangle(5, 5)
        before = str(item)
        item.update()
        self.assertEqual(str(item), before)

    def test_update_args_1(self):
        """Check update args 1."""
        item = Rectangle(5, 5)
        item.update(89)
        self.assertEqual(item.id, 89)

    def test_update_kwargs_1(self):
        """Check update kwargs 1."""
        item = Rectangle(5, 5)
        item.update(**{"id": 89})
        self.assertEqual(item.id, 89)

    def test_create_1(self):
        """Check create 1."""
        item = Rectangle.create(**{"id": 89})
        self.assertEqual(item.id, 89)

    def test_update_args_2(self):
        """Check update args 2."""
        item = Rectangle(5, 5)
        item.update(89, 1)
        self.assertEqual(item.id, 89)
        self.assertEqual(item.width, 1)

    def test_update_kwargs_2(self):
        """Check update kwargs 2."""
        item = Rectangle(5, 5)
        item.update(**{"id": 89, "width": 1})
        self.assertEqual(item.id, 89)
        self.assertEqual(item.width, 1)

    def test_create_2(self):
        """Check create 2."""
        item = Rectangle.create(**{"id": 89, "width": 1})
        self.assertEqual(item.id, 89)
        self.assertEqual(item.width, 1)

    def test_update_args_3(self):
        """Check update args 3."""
        item = Rectangle(5, 5)
        item.update(89, 1, 2)
        self.assertEqual(item.id, 89)
        self.assertEqual(item.width, 1)
        self.assertEqual(item.height, 2)

    def test_update_kwargs_3(self):
        """Check update kwargs 3."""
        item = Rectangle(5, 5)
        item.update(**{"id": 89, "width": 1, "height": 2})
        self.assertEqual(item.id, 89)
        self.assertEqual(item.width, 1)
        self.assertEqual(item.height, 2)

    def test_create_3(self):
        """Check create 3."""
        item = Rectangle.create(**{"id": 89, "width": 1, "height": 2})
        self.assertEqual(item.id, 89)
        self.assertEqual(item.width, 1)
        self.assertEqual(item.height, 2)

    def test_update_args_4(self):
        """Check update args 4."""
        item = Rectangle(5, 5)
        item.update(89, 1, 2, 3)
        self.assertEqual(item.id, 89)
        self.assertEqual(item.width, 1)
        self.assertEqual(item.height, 2)
        self.assertEqual(item.x, 3)

    def test_update_kwargs_4(self):
        """Check update kwargs 4."""
        item = Rectangle(5, 5)
        item.update(**{"id": 89, "width": 1, "height": 2, "x": 3})
        self.assertEqual(item.id, 89)
        self.assertEqual(item.width, 1)
        self.assertEqual(item.height, 2)
        self.assertEqual(item.x, 3)

    def test_create_4(self):
        """Check create 4."""
        item = Rectangle.create(**{"id": 89, "width": 1, "height": 2, "x": 3})
        self.assertEqual(item.id, 89)
        self.assertEqual(item.width, 1)
        self.assertEqual(item.height, 2)
        self.assertEqual(item.x, 3)

    def test_update_args_5(self):
        """Check update args 5."""
        item = Rectangle(5, 5)
        item.update(89, 1, 2, 3, 4)
        self.assertEqual(item.id, 89)
        self.assertEqual(item.width, 1)
        self.assertEqual(item.height, 2)
        self.assertEqual(item.x, 3)
        self.assertEqual(item.y, 4)

    def test_update_kwargs_5(self):
        """Check update kwargs 5."""
        item = Rectangle(5, 5)
        item.update(**{"id": 89, "width": 1, "height": 2, "x": 3, "y": 4})
        self.assertEqual(item.id, 89)
        self.assertEqual(item.width, 1)
        self.assertEqual(item.height, 2)
        self.assertEqual(item.x, 3)
        self.assertEqual(item.y, 4)

    def test_create_5(self):
        """Check create 5."""
        item = Rectangle.create(**{
            "id": 89, "width": 1, "height": 2,
            "x": 3, "y": 4})
        self.assertEqual(item.id, 89)
        self.assertEqual(item.width, 1)
        self.assertEqual(item.height, 2)
        self.assertEqual(item.x, 3)
        self.assertEqual(item.y, 4)


if __name__ == "__main__":
    unittest.main()

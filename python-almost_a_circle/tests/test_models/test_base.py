#!/usr/bin/python3
"""Unit tests for the Base class."""
import json
import os
import tempfile
import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseId(unittest.TestCase):
    """Tests for the id management."""

    def setUp(self):
        """Reset the object counter."""
        Base._Base__nb_objects = 0

    def test_automatic_ids(self):
        """Ids increase by one."""
        self.assertEqual([Base().id, Base().id, Base().id], [1, 2, 3])

    def test_given_id(self):
        """A given id does not change the counter."""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base().id, 2)

    def test_none_id(self):
        """None gives an automatic id."""
        self.assertEqual(Base(None).id, 1)

    def test_zero_and_negative_id(self):
        """Zero and negative ids are kept."""
        self.assertEqual(Base(0).id, 0)
        self.assertEqual(Base(-4).id, -4)

    def test_private_counter(self):
        """The counter is private."""
        with self.assertRaises(AttributeError):
            Base().__nb_objects


class TestBaseJson(unittest.TestCase):
    """Tests for the JSON string methods."""

    def test_to_json_string_none(self):
        """None gives an empty list string."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """An empty list gives an empty list string."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list(self):
        """A list of dictionaries is serialized."""
        data = [{"id": 1, "width": 2}]
        result = Base.to_json_string(data)
        self.assertIsInstance(result, str)
        self.assertEqual(json.loads(result), data)

    def test_from_json_string_none(self):
        """None gives an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """An empty string gives an empty list."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_empty_list(self):
        """An empty list string gives an empty list."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_list(self):
        """A JSON string is deserialized."""
        self.assertEqual(Base.from_json_string('[{"id": 89}]'), [{"id": 89}])


class TestBaseCreate(unittest.TestCase):
    """Tests for the create method."""

    def test_create_rectangle(self):
        """A rectangle is rebuilt from its dictionary."""
        original = Rectangle(3, 5, 1, 2, 7)
        copy = Rectangle.create(**original.to_dictionary())
        self.assertIsNot(original, copy)
        self.assertEqual(str(original), str(copy))

    def test_create_square(self):
        """A square is rebuilt from its dictionary."""
        original = Square(3, 1, 2, 7)
        copy = Square.create(**original.to_dictionary())
        self.assertIsNot(original, copy)
        self.assertEqual(str(original), str(copy))

    def test_create_only_id(self):
        """Only the given attributes are changed."""
        self.assertEqual(Rectangle.create(id=89).id, 89)
        self.assertEqual(Square.create(id=89).size, 1)


class TestBaseFiles(unittest.TestCase):
    """Tests for saving to and loading from files."""

    def setUp(self):
        """Work in an empty temporary directory."""
        self.old_directory = os.getcwd()
        self.directory = tempfile.TemporaryDirectory()
        os.chdir(self.directory.name)

    def tearDown(self):
        """Return to the original directory."""
        os.chdir(self.old_directory)
        self.directory.cleanup()

    def read(self, name):
        """Return the data stored in a JSON file."""
        with open(name, "r", encoding="utf-8") as f:
            return json.load(f)

    def test_save_none(self):
        """None saves an empty list."""
        Rectangle.save_to_file(None)
        self.assertEqual(self.read("Rectangle.json"), [])

    def test_save_empty(self):
        """An empty list is saved."""
        Square.save_to_file([])
        self.assertEqual(self.read("Square.json"), [])

    def test_save_rectangles(self):
        """Rectangles are saved."""
        items = [Rectangle(10, 7, 2, 8), Rectangle(2, 4)]
        Rectangle.save_to_file(items)
        self.assertEqual(self.read("Rectangle.json"),
                         [item.to_dictionary() for item in items])

    def test_save_squares(self):
        """Squares are saved."""
        items = [Square(5), Square(7, 9, 1)]
        Square.save_to_file(items)
        self.assertEqual(self.read("Square.json"),
                         [item.to_dictionary() for item in items])

    def test_save_overwrites(self):
        """An existing file is overwritten."""
        Square.save_to_file([Square(5)])
        Square.save_to_file([])
        self.assertEqual(self.read("Square.json"), [])

    def test_load_missing_file(self):
        """A missing file gives an empty list."""
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])

    def test_load_rectangles(self):
        """Rectangles are loaded."""
        items = [Rectangle(10, 7, 2, 8), Rectangle(2, 4)]
        Rectangle.save_to_file(items)
        loaded = Rectangle.load_from_file()
        self.assertTrue(all(type(item) is Rectangle for item in loaded))
        self.assertEqual([str(i) for i in loaded], [str(i) for i in items])

    def test_load_squares(self):
        """Squares are loaded."""
        items = [Square(5), Square(7, 9, 1)]
        Square.save_to_file(items)
        loaded = Square.load_from_file()
        self.assertTrue(all(type(item) is Square for item in loaded))
        self.assertEqual([str(i) for i in loaded], [str(i) for i in items])


if __name__ == "__main__":
    unittest.main()

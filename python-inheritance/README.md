# python-inheritance

Inheritance in Python: `dir`, subclassing built-in types, `type`, `isinstance` and `issubclass`, overriding methods, and `super()`.

## Files

| File | Description |
| --- | --- |
| `0-lookup.py` | Returns the list of attributes and methods of an object |
| `1-my_list.py` | `MyList`, a subclass of `list` with a `print_sorted()` method |
| `2-is_same_class.py` | Returns `True` if an object is exactly an instance of a class |
| `3-is_kind_of_class.py` | Returns `True` if an object is an instance of a class or of a subclass of it |
| `4-inherits_from.py` | Returns `True` if an object is an instance of a subclass of a class (not the class itself) |
| `5-base_geometry.py` | An empty `BaseGeometry` class |
| `6-base_geometry.py` | `BaseGeometry` with an `area()` method that is not implemented |
| `7-base_geometry.py` | `BaseGeometry` with an `integer_validator()` method |
| `8-rectangle.py` | `Rectangle` inheriting from `BaseGeometry`, with a validated private width and height |
| `9-rectangle.py` | `Rectangle` with `area()` and a `[Rectangle] <width>/<height>` description |
| `10-square.py` | `Square` inheriting from `Rectangle` |
| `11-square.py` | `Square` with a `[Square] <width>/<height>` description |
| `tests/1-my_list.txt` | Doctests for `1-my_list.py` |
| `tests/7-base_geometry.txt` | Doctests for `7-base_geometry.py` |

## Running the tests

```
$ python3 -m doctest -v ./tests/1-my_list.txt
$ python3 -m doctest -v ./tests/7-base_geometry.txt
```

## Usage

```
$ cat 11-main.py
#!/usr/bin/python3
Square = __import__('11-square').Square

s = Square(13)

print(s)
print(s.area())

$ ./11-main.py
[Square] 13/13
169
```

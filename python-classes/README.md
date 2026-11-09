# python-classes

Defining classes in Python: private attributes, validation, properties (getters and setters) and instance methods.

## Files

| File | Description |
| --- | --- |
| `0-square.py` | An empty `Square` class |
| `1-square.py` | `Square` with a private `size` attribute set at instantiation |
| `2-square.py` | `Square` that validates `size` (type and value) when instantiated |
| `3-square.py` | `Square` with an `area()` method |
| `4-square.py` | `Square` with a `size` property, getter and validating setter |
| `5-square.py` | `Square` with a `my_print()` method that prints the square with `#` |
| `6-square.py` | `Square` with a validated `position` property used by `my_print()` |

## Usage

```
$ cat 5-main.py
#!/usr/bin/python3
Square = __import__('5-square').Square

my_square = Square(3)
my_square.my_print()

$ ./5-main.py
###
###
###
```

# python-more_classes

More on classes in Python: properties, string representations, class attributes, static methods and class methods.

## Files

| File | Description |
| --- | --- |
| `0-rectangle.py` | An empty `Rectangle` class |
| `1-rectangle.py` | `Rectangle` with validated `width` and `height` properties |
| `2-rectangle.py` | Adds `area()` and `perimeter()` |
| `3-rectangle.py` | Adds `__str__` to draw the rectangle with `#` |
| `4-rectangle.py` | Adds `__repr__` so `eval(repr(r))` recreates the rectangle |
| `5-rectangle.py` | Prints `Bye rectangle...` when an instance is deleted |
| `6-rectangle.py` | Adds the class attribute `number_of_instances` |
| `7-rectangle.py` | Adds the class attribute `print_symbol` used to draw the rectangle |
| `8-rectangle.py` | Adds the static method `bigger_or_equal()` comparing areas |
| `9-rectangle.py` | Adds the class method `square()` |

## Usage

```
$ cat 9-main.py
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)

$ ./9-main.py
Area: 25 - Perimeter: 20
#####
#####
#####
#####
#####
Bye rectangle...
```

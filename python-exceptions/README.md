# python-exceptions

Handling and raising exceptions in Python with `try` / `except` / `finally` and `raise`.

## Files

| File | Description |
| --- | --- |
| `0-safe_print_list.py` | Prints `x` elements of a list and returns the number actually printed |
| `1-safe_print_integer.py` | Prints an integer with `"{:d}".format()` and returns whether it worked |
| `2-safe_print_list_integers.py` | Prints the first `x` elements of a list, skipping anything that is not an integer |
| `3-safe_print_division.py` | Divides two integers and prints the result in the `finally` block |
| `4-list_division.py` | Divides two lists element by element, reporting wrong type, division by 0 and out of range |
| `5-raise_exception.py` | Raises a `TypeError` |
| `6-raise_exception_msg.py` | Raises a `NameError` with a message |

## Usage

```
$ cat 3-main.py
#!/usr/bin/python3
safe_print_division = __import__('3-safe_print_division').safe_print_division

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

$ ./3-main.py
Inside result: 6.0
12 / 2 = 6.0
Inside result: None
12 / 0 = None
```

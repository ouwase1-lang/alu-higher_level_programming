# python-import_modules

Importing functions and variables from other Python files, and using command-line arguments.

## Files

| File | Description |
| --- | --- |
| `0-add.py` | Imports `add` from `add_0.py` and prints `1 + 2 = 3` |
| `1-calculation.py` | Imports add, sub, mul and div from `calculator_1.py` and prints the results |
| `2-args.py` | Prints the number of arguments and the list of them |
| `3-infinite_add.py` | Prints the sum of all arguments |
| `4-hidden_discovery.py` | Prints the names defined in the compiled module `hidden_4.pyc` (needs Python 3.8) |
| `5-variable_load.py` | Imports the variable `a` from `variable_load_5.py` and prints it |
| `add_0.py`, `calculator_1.py`, `variable_load_5.py` | Helper modules imported by tasks 0, 1 and 5 |

## Usage

```
$ ./2-args.py Hello Welcome
2 arguments:
1: Hello
2: Welcome
$ ./3-infinite_add.py 79 10 -40
49
```

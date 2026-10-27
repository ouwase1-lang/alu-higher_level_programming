# python-data_structures

Working with lists, tuples and strings in Python: indexing, slicing, copying, and returning multiple values.

## Files

| File | Description |
| --- | --- |
| `0-print_list_integer.py` | Prints all integers of a list, one per line |
| `1-element_at.py` | Retrieves an element from a list, returning `None` if the index is out of range |
| `2-replace_in_list.py` | Replaces an element of a list at a given position |
| `3-print_reversed_list_integer.py` | Prints all integers of a list in reverse order |
| `4-new_in_list.py` | Replaces an element in a copy of a list, leaving the original unchanged |
| `5-no_c.py` | Removes all `c` and `C` characters from a string |
| `6-print_matrix_integer.py` | Prints a matrix of integers |
| `7-add_tuple.py` | Adds the first two elements of two tuples |
| `8-multiple_returns.py` | Returns a tuple with the length of a string and its first character |
| `9-max_integer.py` | Finds the biggest integer of a list without using `max()` |
| `10-divisible_by_2.py` | Returns a list of booleans: whether each integer is a multiple of 2 |
| `11-delete_at.py` | Deletes the item at a given position in a list |
| `12-switch.py` | Switches the values of `a` and `b` |

## Usage

```
$ cat 0-main.py
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

$ ./0-main.py
1
2
3
4
5
$ ./12-switch.py
a=10 - b=89
```

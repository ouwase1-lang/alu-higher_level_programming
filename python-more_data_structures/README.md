# python-more_data_structures

Working with sets, dictionaries, list comprehensions and `map` in Python.

## Files

| File | Description |
| --- | --- |
| `0-square_matrix_simple.py` | Returns a new matrix with the square of every value |
| `1-search_replace.py` | Returns a new list with all occurrences of an element replaced |
| `2-uniq_add.py` | Adds all unique integers of a list |
| `3-common_elements.py` | Returns the set of elements present in both sets |
| `4-only_diff_elements.py` | Returns the set of elements present in only one of two sets |
| `5-number_keys.py` | Returns the number of keys in a dictionary |
| `6-print_sorted_dictionary.py` | Prints a dictionary ordered by key |
| `7-update_dictionary.py` | Replaces or adds a key/value in a dictionary |
| `8-simple_delete.py` | Deletes a key in a dictionary |
| `9-multiply_by_2.py` | Returns a new dictionary with all values multiplied by 2 |
| `10-best_score.py` | Returns the key with the biggest integer value |
| `11-multiply_list_map.py` | Returns a new list with all values multiplied by a number, using `map` |
| `12-roman_to_int.py` | Converts a Roman numeral to an integer |

## Usage

```
$ cat 0-main.py
#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

$ ./0-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

# python-input_output

Python exercises on file input/output and JSON serialization.

## Files

| File | Description |
| --- | --- |
| `0-read_file.py` | `read_file(filename="")`: reads a UTF8 text file and prints it to stdout. |
| `1-write_file.py` | `write_file(filename="", text="")`: writes a string to a file (overwrites) and returns the number of characters written. |
| `2-append_write.py` | `append_write(filename="", text="")`: appends a string to a file (creates it if needed) and returns the number of characters added. |
| `3-to_json_string.py` | `to_json_string(my_obj)`: returns the JSON representation of an object. |
| `4-from_json_string.py` | `from_json_string(my_str)`: returns the object represented by a JSON string. |
| `5-save_to_json_file.py` | `save_to_json_file(my_obj, filename)`: writes an object to a file as JSON. |
| `6-load_from_json_file.py` | `load_from_json_file(filename)`: creates an object from a JSON file. |
| `7-add_item.py` | Script that adds all arguments to a list and saves it to `add_item.json`. |
| `8-class_to_json.py` | `class_to_json(obj)`: returns the dictionary description of an object for JSON serialization. |
| `9-student.py` | `Student` class with a `to_json` method. |
| `10-student.py` | `Student` class with `to_json(attrs=None)` that can filter attributes. |
| `11-student.py` | `Student` class with `to_json` and `reload_from_json`. |
| `12-pascal_triangle.py` | `pascal_triangle(n)`: returns Pascal's triangle of `n` as a list of lists. |

## Requirements

- Python 3, interpreted on Ubuntu
- All files start with `#!/usr/bin/python3`
- Code follows the `pycodestyle` style
- All modules and functions are documented

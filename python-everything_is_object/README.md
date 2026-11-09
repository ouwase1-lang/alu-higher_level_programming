# python-everything_is_object

Everything is an object in Python: `id` and `type`, mutable and immutable objects, aliases, and how arguments are passed to functions.

## Files

| File | Description |
| --- | --- |
| `0-answer.txt` to `18-answer.txt` | Answers to the questions on `type`, `id`, `is` / `==`, aliasing and passing arguments to functions |
| `19-copy_list.py` | Returns a copy of a list |
| `20-answer.txt` to `28-answer.txt` | Answers to the questions on tuples, empty tuples and `id` after list operations |

## Usage

```
$ cat 19-main.py
#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
new_list = copy_list(my_list)

print(new_list == my_list)
print(new_list is my_list)

$ ./19-main.py
True
False
```

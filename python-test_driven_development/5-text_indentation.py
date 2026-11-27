#!/usr/bin/python3
"""
Module 5-text_indentation.

Provides the function text_indentation(text).
"""


def text_indentation(text):
    """Print text with 2 new lines after each ".", "?" and ":".

    Printed lines have no leading or trailing spaces."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = ""
    for char in text:
        if char == "\n":
            print(line.strip(" "))
            line = ""
            continue
        line += char
        if char in ".?:":
            print(line.strip(" "), end="\n\n")
            line = ""
    print(line.strip(" "), end="")

#!/usr/bin/python3
"""Displays the body of the response from a URL or the HTTP error code."""
from sys import argv
from urllib import error, request


if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))

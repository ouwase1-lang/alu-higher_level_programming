#!/usr/bin/python3
"""Displays the X-Request-Id header value of the response from a URL."""
from sys import argv
from urllib import request


if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        print(response.headers.get("X-Request-Id"))

#!/usr/bin/python3
"""Sends a POST request with an email to a URL and displays the body."""
from sys import argv
from urllib import parse, request


if __name__ == "__main__":
    data = parse.urlencode({"email": argv[2]}).encode("ascii")
    with request.urlopen(request.Request(argv[1], data)) as response:
        print(response.read().decode("utf-8"))

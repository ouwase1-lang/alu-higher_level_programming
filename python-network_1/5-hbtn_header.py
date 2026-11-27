#!/usr/bin/python3
"""Displays the X-Request-Id header value of the response from a URL."""
from sys import argv
import requests


if __name__ == "__main__":
    response = requests.get(argv[1])
    print(response.headers.get("X-Request-Id"))

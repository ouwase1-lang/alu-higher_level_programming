#!/usr/bin/python3
"""Displays a GitHub user id using Basic Authentication."""
from sys import argv
import requests


if __name__ == "__main__":
    response = requests.get("https://api.github.com/user",
                            auth=(argv[1], argv[2]))
    print(response.json().get("id"))

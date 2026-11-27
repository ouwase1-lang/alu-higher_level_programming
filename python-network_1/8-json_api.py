#!/usr/bin/python3
"""Searches for a user by sending a letter in a POST request."""
from sys import argv
import requests


if __name__ == "__main__":
    letter = argv[1] if len(argv) > 1 else ""
    response = requests.post("http://0.0.0.0:5000/search_user",
                             data={"q": letter})
    try:
        user = response.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if user:
            print("[{}] {}".format(user.get("id"), user.get("name")))
        else:
            print("No result")

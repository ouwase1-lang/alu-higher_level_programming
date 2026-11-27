#!/bin/bash
# Send a GET request to a URL and display the body only on a 200 status code
tmp=$(mktemp); [ "$(curl -sL -o "$tmp" -w '%{http_code}' "$1")" = "200" ] && cat "$tmp"; rm -f "$tmp"

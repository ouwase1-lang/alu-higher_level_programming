#!/bin/bash
# Display the size in bytes of the response body of a URL
curl -s "$1" | wc -c

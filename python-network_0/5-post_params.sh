#!/bin/bash
# Send a POST request with email and subject variables and display the body
curl -s -X POST --data-urlencode "email=test@gmail.com" --data-urlencode "subject=I will always be here for PLD" "$1"

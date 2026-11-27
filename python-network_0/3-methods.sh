#!/bin/bash
# Display all HTTP methods the server of a URL will accept
curl -s -i -X OPTIONS "$1" | grep -i '^Allow:' | cut -d ' ' -f 2- | tr -d '\r'

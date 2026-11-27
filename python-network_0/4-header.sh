#!/bin/bash
# Send a GET request with a custom header and display the response body
curl -s -H "X-HolbertonSchool-User-Id: 98" -H "X-School-User-Id: 98" "$1"

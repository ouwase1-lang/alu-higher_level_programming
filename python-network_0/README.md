# python-network_0

Bash scripts that use `curl` to send HTTP requests. Each takes a URL as its first argument.

- `0-body_size.sh`: displays the size of the response body in bytes
- `1-body.sh`: sends a GET request and displays the body of a 200 response
- `2-delete.sh`: sends a DELETE request and displays the body
- `3-methods.sh`: displays the HTTP methods the server accepts
- `4-header.sh`: sends a GET request with the headers `X-HolbertonSchool-User-Id: 98` and `X-School-User-Id: 98`
- `5-post_params.sh`: sends a POST request with `email` and `subject` variables

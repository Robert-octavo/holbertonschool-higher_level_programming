#!/bin/bash
# Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response https://reqbin.com/req/c-1dw4uds4/curl-delete-request-example
curl -s "$1" -X DELETE

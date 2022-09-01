#!/bin/bash
# Write a Bash script that takes in a URL, sends a GET request
# to the URL, and displays the body of the response
# https://reqbin.com/req/c-1n4ljxb9/curl-get-request-example
curl -s "$1" -X GET -L echo""

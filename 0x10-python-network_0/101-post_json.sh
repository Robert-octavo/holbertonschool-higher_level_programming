#!/bin/bash
# Write a Bash script that sends a JSON POST request to a URL passed as the first argument,
# and displays the body of the response.
# https://reqbin.com/req/c-dwjszac0/curl-post-json-example
# curl -X POST https://reqbin.com/echo/post/json -d @filename  @ add a file name

curl -s -X POST --header 'Content-Type: application/json' --data @"$2" "$1"

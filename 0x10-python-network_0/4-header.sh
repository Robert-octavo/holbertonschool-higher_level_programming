#!/bin/bash
# Write a Bash script that takes in a URL as an argument, sends a GET request
# to the URL, and displays the body of the response
# https://akrabat.com/view-header-and-body-with-curl/
# https://curl.se/docs/manpage.html

curl -s -X GET --header "X-HolbertonSchool-User-Id: 98" "$1"
